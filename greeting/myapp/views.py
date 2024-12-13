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
  



class FeedBackView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"Feedback.html")
    
    def post(self,request,*args,**kwargs):

        name=request.POST.get("username")
        mail=request.POST.get("email")
        msg=request.POST.get("feedback")

        print(name)
        print(mail)
        print(msg)

        print("inside post")
        return render(request,"Feedback.html")
        

class ReviewView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"review.html")
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        product=form_data.get("product")

        rating=form_data.get("rating")

        comment=form_data.get("comment")


        print(product)
        print(comment)
        print(rating)

        return render(request,"review.html")
    




class FilimReview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"filim_reviw.html")
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        filim=form_data.get("fname")

        comment=form_data.get("comment")

        review=form_data.get("review")

        print(filim)
        print(review)
        print(comment)

        return render(request,"filim_reviw.html")
    

        
class FacultyReview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"faculty_review.html")
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        email=form_data.get("email")

        faculty_name=form_data.get("facname")

        course_name=form_data.get("course")

        comment=form_data.get("comment")

        print(email)

        print(faculty_name)

        print(course_name)

        print(comment)

        return render(request,"faculty_review.html")


