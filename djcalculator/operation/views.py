from django.shortcuts import render
from django.views.generic import View

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