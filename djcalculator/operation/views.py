from django.shortcuts import render
from django.views.generic import View
from operation.forms import VehicleForm
from operation.forms import SingUpForm
from operation.forms import AppoinmentRequestForm
from operation.forms import BmiForm
from operation.forms import MilageForm
from operation.forms import EmiForm,CalorieForm


# Create your views here.

class AdditionView(View):
    
    def get(self,request,*args,**kwargs):

        return render(request,"addition.html")
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get("num1")

        num2=form_data.get("num2")

        result=int(num1)+int(num2)

        # print(result)

        data={
            "output":result
        }


        return render(request,"addition.html",data)
    

class SubtractionView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"sub.html")
    

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get("num1")

        num2=form_data.get("num2")


        result=int(num1)-int(num2)

        data={
            "output":result
        }


        return render(request,"sub.html",data)
    
class MultiplicationView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"multi.html")
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        num1=form_data.get("num1")

        num2=form_data.get("num2")


        result=int(num1)*int(num2)

        data={
            "output":result
        }


        return render(request,"multi.html",data)
    

class VehichleRegistrationView(View):
    def get(self,request,*args,**kwargs):

        form_instance=VehicleForm()

        context={
            "form":form_instance
        }

        return render(request,"vehicle.html",context)
    

# class BMRView(View):

class SingUpView(View):
    def get(self,request,*args,**keargs):

        form_instance=SingUpForm()

        context={
            "form":form_instance
        }

        return render(request,"Signup.html",context)
    


class AppointmentRequestFormView(View):
    def get(self,request,*args,**kwargs):

        form_instance=AppoinmentRequestForm()

        context={
            "form":form_instance
        }


        return render(request,"Appoiinment.html",context)
    
class BmiFormView(View):
    def get(self,request,*args,**kwargs):

        form_instance=BmiForm()

        context={
            "form":form_instance
        }

        return render(request,"bmi.html",context)
    

    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BmiForm(form_data)

        if form_instance.is_valid():


            data=form_instance.cleaned_data

            height=data.get("height")

            weight=data.get("weight")

            bmi=weight//(height/100)**2
            
            print(bmi)

            

        return render(request,"bmi.html",{"form":form_instance,"result":bmi})
    
class MilageFormView(View):
    def get(self,request,*args,**kwargs):

        form_instance=MilageForm()

        context={
            "form":form_instance
        }

        return render(request,"milage.html",context)
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=MilageForm(form_data)
        
        if form_instance.is_valid():

            data=form_instance.cleaned_data

            distance=data.get("distance")

            consumption=data.get("consumption")

            milage=distance/consumption

        return render(request,"milage.html",{"form":form_instance,"result":milage})
    
class EmiFormView(View):
    def get(self, request, *args, **kwargs):
        # Instantiate an empty form for the GET request
        form_instance = EmiForm()  

        context = {
            "form": form_instance
        }

        return render(request, "emi.html", context)

    def post(self, request, *args, **kwargs):
        form_data = request.POST
        form_instance = EmiForm(form_data)

       
        if form_instance.is_valid():
            data = form_instance.cleaned_data

            amount = data.get("amount")  
            interest = data.get("interest")  
            tenure = data.get("tenure")  

           
            monthly_interest = interest / (12 * 100)

            
            tenure_months = tenure * 12

            numerator = amount * monthly_interest * (1 + monthly_interest) ** tenure_months
            denominator = (1 + monthly_interest) ** tenure_months - 1
            result = numerator / denominator if denominator != 0 else 0

        return render(request, "emi.html", {"form": form_instance, "result": result})


class CalorieFormView(View):
    def get(self,request,*args,**kwargs):

        form_instance=CalorieForm()

        context={
            "form":form_instance
        }
        return render(request,"calorie.html",context)
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=CalorieForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data\
            

            # print(data)

            weight=data.get("weight")

            height=data.get("height")

            age=data.get("age")

            gender=data.get("gender")

            if gender=="male":

                BMR=10*weight+6.25*height-5*age+5

            else:

                BMR=10*weight+6.25*height-5*age-161

            activity_level=data.get("activity_level")

            Calorie=BMR*float(activity_level)
            
            
        
        return render(request,"calorie.html",{"form":form_instance,"result":BMR,"Calorie":Calorie})










    
