from django.shortcuts import render,redirect

from django.views.generic import View,TemplateView,FormView

from django.contrib.auth import authenticate,login
# Create your views here.
from django.urls import reverse_lazy

from student.forms import StudentCreationForm,SigninForm

from instructor.models import Course,Cart,Order,Module,Lesson

from django.db.models import Sum

import razorpay


RZP_KEY_ID="rzp_test_iECXJsyaNCg372"

RZP_KEY_SECRET="SahbuXWwD6UpsKbMrxA43FPD"





class StudentAddView(View):

    def get(self,request,*args,**kwargs):

        form_instance=StudentCreationForm()

        return render(request,"student.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=StudentCreationForm(form_data)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("signin")
        
        else:
            return render(request,"student.html",{"form":form_instance})
        

class SigninView(FormView):

    # def get(self,request,*args,**kwargs):

        # form_instance=SigninForm()

        # return render(request,"",{"form":form_instance})

    template_name="signin.html"
    form_class=SigninForm

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SigninForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_obj=authenticate(request,username=uname,password=pwd)

            if user_obj:

                login(request,user_obj)

                print("success")

                return redirect("index")
            else:

                print("invalid")
                return render(request,"student.html")

       
            
        
class IndexView(View):
    
    def get(self,request,*args,**kwargs):

        all_courses=Course.objects.all()

        purchased_courses=Order.objects.filter(student=request.user).values_list("course_objects",flat=True)

        return render(request,"index.html",{"courses":all_courses,"purchased_courses":purchased_courses})




class CourseDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        course_instance=Course.objects.get(id=id)


        return render(request,"Course.html",{"course":course_instance})
     
        

        
class AddToCartView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        course_instance=Course.objects.get(id=id)

        user_instance=request.user

        
        # Cart.objects.create(course_object=course_instance,user=user_instance)

        cart_instance,created=Cart.objects.get_or_create(course_object=course_instance,user=user_instance)

        print(created)
        return redirect("cart-summery")
    

class CartSummeryView(View):

    def get(self,request,*args,**kwargs):

        qs=request.user.basket.all()

        cart_summery=qs.values("course_object__price").aggregate(total=Sum("course_object__price")).get("total")

        print(cart_summery)

        return render(request,"cart-summery.html",{"carts":qs,"basket_total":cart_summery})
    
class CartItemDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Cart.objects.get(id=id).delete()

        return redirect("cart-summery")
    

class CheckOutView(View):

    def get(self,request,*args,**kwargs):

        cart_items=request.user.basket.all()

        order_totlal=sum([ci.course_object.price for ci in cart_items])

        order_instance=Order.objects.create(student=request.user,total=order_totlal)

        for ci in cart_items:

            order_instance.course_objects.add(ci.course_object)

            ci.delete()

        order_instance.save()

        if order_totlal>0:
            client = razorpay.Client(auth=(RZP_KEY_ID,RZP_KEY_SECRET))

            data = { "amount": int(order_totlal*100), "currency": "INR", "receipt": "order_rcptid_11" }

            payment = client.order.create(data=data)

            print(payment,"*************************************")

            rzp_id=payment.get("id")

            order_instance.rzp_order_id=rzp_id

            order_instance.save()

            context={
                "rzp_key_id":RZP_KEY_ID,
                "amount":int(order_totlal*100),
                "rzp_order_id":rzp_id,


            }

            return render(request,"payment.html",context)
        

        return redirect("index")
    

class MyCoursesView(View):

    def get(self,request,*args,**kwargs):

        Courses=request.user.purchase.all()
        print(Courses)

        return render(request,"Mycourese.html",{"orders":Courses})
    
#Localhost:8000/student/Courses/1/watch?module-1&lesson-4
class LessonDetailView(View):

    def get(self,request,*args,**kwargs):

       course_id=kwargs.get("pk")

       course_instance=Course.objects.get(id=course_id) 

    #    request.GET={"module":1,"lesson":1}
       query_params=request.GET

       module_id=query_params.get("module") if "module" is query_params else course_instance.modules.all().first().id

       

       module_instance=Module.objects.get(id=module_id,course_object=course_instance)
       
       lesson_id=query_params.get("lesson") if "lesson" is query_params else module_instance.lessons.all().first().id
       lesson_instance=Lesson.objects.get(id=lesson_id,module_object=module_instance)


       return render(request,"lesson_details.html",{"course":course_instance,"lesson":lesson_instance})
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name="dispatch")

class PaymentVerificationView(View):

    def post(self,request,*args,**kwargs):

        print(request.POST,"******************~!!!!!!!!@@@@@@@@@")
        

        return redirect("index")