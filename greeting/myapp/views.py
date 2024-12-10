from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class HelloworldView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"Helloworld.html")
    
class GoodmorningView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"good_morning.html")
    
class GoodnightView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"good_night.html")

class GoodafternoonView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"good_afternoon.html")
    
class GoodeveningView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"goodevening.html")
    


class MohanlalViwe(View):

    def get(self,request,*args,**kwargs):
        
        data={"name":"Mohanlal",
              "age":64,
              "number_of_movies":300,
        }

        return render(request,"mohanlal.html",data)
    

class MammoottyViwe(View):

    def get(self,request,*args,**kwargs):
        
        data={"name":"Mammootty",
              "age":73,
              "number_of_movies":400,
        }

        return render(request,"mammootty.html",data)
    
class RobertDowneyJrView(View):
    def get(self,request,*args,**kwargs):

        data={"name":"Robert John Downey Jr",
              "age":59,
              "number_of_movies":95,
        }

        return render(request,"rdj.html",data)
    

class KamalHaasanView(View):
    def get(self,request,*args,**kwargs):

        data={"name":"Kamal Haasan",
              "age":70,
              "number_of_movies":200,
        }

        return render(request,"Kamal_Haasan.html",data)
    
class RajinikanthView(View):
    def get(self,request,*args,**kwargs):

        data={"name":"Rajinikanth",
              "age":73,
              "number_of_movies":170,
        }

        return render(request,"Rajinikanth.html",data)



    # Kamal Haasan

    # Rajinikanth



