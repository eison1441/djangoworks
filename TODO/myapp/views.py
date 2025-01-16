from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import SignUpForm
from myapp.forms import SignInForm
from myapp.forms import AddProjectForm
from myapp.models import Todo
from django.db.models import Q

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.db.models import Count

class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignUpForm()

        return render(request,"register.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SignUpForm(form_data)

        if form_instance.is_valid():

            form_instance.save()

            print(">>>>>>>>acc created<<<<<<<<<<<")

            return redirect("login")
        
        else:

            print(">>>>>>>>faild!!<<<<<<<<<")


            return render(request,"register.html",{"form":form_instance})

class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=(SignInForm)

        return render(request,"login.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SignInForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_instance=authenticate(request,username=uname,password=pwd)

            if user_instance:

                login(request,user_instance)

                print(">>>>>>>>>session started<<<<<<<<<<")

                return redirect("index") 
            else:

                print(">>>>>>faild<<<<<<<<<<")

                return render(request,"login.html",{"form":form_instance})  
    
class IndexView(View):

    def get(self,request,*args,**kwargs):

        

        category_summary=Todo.objects.filter(owner=request.user).values("category").annotate(count=Count("category"))
        print(category_summary)
        context ={
            "category_dict":category_summary,

            
        }
        priority_summary=Todo.objects.filter(owner=request.user).values("priority").annotate(count=Count("priority"))

        print(priority_summary)

        status_summary=Todo.objects.filter(owner=request.user).values("status").annotate(count=Count("status"))

        print(status_summary)

        return render(request,"index.html",context) 
    
class ProjectAddView(View):

    def get(self,request,*args,**kwargs):

        form_instance=AddProjectForm()

        return render(request,"addproject.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=AddProjectForm(form_data)
        if form_instance.is_valid():

            form_instance.instance.owner=request.user
            form_instance.save()
            
            # data=form_instance.cleaned_data
            # Todo.objects.create(**data,owner=request.user)

            return redirect("addproject")
        else:
            print(">>>>failed")
            return render(request,"addproject.html",{"form":form_instance})
        

class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("login")
        

class ProjectListView(View):

    def get(self,request,*args,**kwargs):

        qs=Todo.objects.all()

        return render(request,"project_list.html",{"data":qs})
    
class ProjectDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Todo.objects.get(id=id).delete()

        return redirect("projectlist")
    

class ProjectUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        project_obj=Todo.objects.get(id=id)

        form_instance=AddProjectForm(instance=project_obj)

        return render(request,"project_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        project_obj=Todo.objects.get(id=id)

        form_data=request.POST

        form_instance=AddProjectForm(form_data,instance=project_obj)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("addproject")
        
        else:

            return render(request,"project_edit.html",{"form":form_instance})

    