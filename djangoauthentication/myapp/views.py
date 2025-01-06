from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.views.generic import View

from myapp.forms import SignUpForm,SignInForm

from django.contrib.auth import authenticate,login,logout

# Create your views here.


class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignUpForm()

        return render(request,"Signup.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SignUpForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data)

            print(">>>>>>>>account created <<<<<<<<<<<<")

            return redirect("signin")
        print(">>>>>>>>>>faild<<<<<<<<<<<<")

        return render(request,"Signup.html",{"form":form_instance})


class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignInForm()

        return render(request,"signin.html",{"form":form_instance})
            

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SignInForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data


            uname=data.get("username")

            pwd=data.get("password")


            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                print(request.user)

                return redirect("index")
                

            else:
                print("invalid")

            

            return redirect("signin")
        
class IndexView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"index.html")
    


class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")

