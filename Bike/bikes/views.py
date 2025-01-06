from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
from django.views.generic import View

from bikes.forms import BikeAddForm,BikeSignUpForm,BikeSignInForm

from bikes.models import Bike

from django.db.models import Q

from django.contrib.auth.models import User



    
class BikeAddView(View):
    def get(self,request,*args,**kwargs):

        form_instance=BikeAddForm()

        return render(request,"Bike_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BikeAddForm(form_data,files=request.FILES)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Bike.objects.create(
                name=data.get("name"),
                brand=data.get("brand"),
                price=data.get("price"),
                fuel_type=data.get("fuel_type"),
                color=data.get("color"),
                mileage=data.get("mileage"),
                image=data.get("image")
            )
            return redirect("Bike_list")
        return render(request,"Bike_add.html",{"form":form_instance})
    
class BikeListView(View):

    def get(self,request,*args,**kwargs):

        search_text=request.GET.get("search")

        print(search_text)

        qs=Bike.objects.all()

        if search_text:

            qs=qs.filter(Q(name__contains=search_text)|Q(brand__contains=search_text))


        return render(request,"Bike_list.html",{"data":qs})
    
class BikeDetailsView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Bike.objects.get(id=id)

        return render(request,"Bike_Details.html",{"data":qs})
    
class BikeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Bike.objects.get(id=id).delete()

        return redirect("Bike_list")
# class BikeUpdateView(View):

#     def get(self,request,*args,**kwargs):

#         id=kwargs.get("pk")

#         bike_obj=Bike.objects.get(id=id)

#         bike_dict={

#             "name":bike_obj.name,
#             "brand":bike_obj.brand,
#             "price":bike_obj.price,
#             "fuel_type":bike_obj.fuel_type,
#             "color":bike_obj.color,
#             "mileage":bike_obj.mileage,
#             # "image":bike_dict.image

#         }

#         form_instance=BikeAddForm(initial=bike_dict)
        

#         return render(request,"bike_update.html",{"form":form_instance})
    
#     def post(self,request,*args,**kwargs):

#         form_data=request.POST

#         id=kwargs.get("pk")


#         bike_obj=Bike.objects.get(id=id)

        
#         form_instance=BikeAddForm(form_data,files=request.FILES,instance=bike_obj)

#         id=kwargs.get("pk")

#         if form_instance.is_valid():
#             data=form_instance.cleaned_data
            

#             Bike.objects.filter(id=id).update(**data)

#             #print("form inst",form_instance)


#             return redirect("Bike_list")
        
#         return render(request,"bike_update.html",{"form":form_instance})\

class BikeUpdateView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        bike_obj = get_object_or_404(Bike, id=id)
        bike_dict = {
            "name": bike_obj.name,
            "brand": bike_obj.brand,
            "price": bike_obj.price,
            "fuel_type": bike_obj.fuel_type,
            "color": bike_obj.color,
            "mileage": bike_obj.mileage,
            "image": bike_obj.image,
        }
        form_instance = BikeAddForm(initial=bike_dict)
        return render(request, "bike_update.html", {"form": form_instance})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        bike_obj = get_object_or_404(Bike, id=id)
        form_instance = BikeAddForm(request.POST, request.FILES, instance=bike_obj)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("Bike_list")
        return render(request, "bike_update.html", {"form": form_instance})
    


class BikeSignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BikeSignUpForm()

        return render(request,"bikesignup.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BikeSignUpForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data)

            print(">>>>>>>>>>account created <<<<<<<<<<<")

            return redirect("signin")
        
        print(">>>>>>>>faild!!!!<<<<<<<<<<<<<")
        return render(request,"bikesignup.html",{"form":form_instance})
    
class BikeSignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BikeSignInForm()

        return render(request,"bikesignin.html",{"form":form_instance})
            

            

    


         