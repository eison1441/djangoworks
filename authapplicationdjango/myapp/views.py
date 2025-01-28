from django.shortcuts import render,redirect

from myapp.forms import SignUpForm,SigninForm,UserProfileForm

from django.views.generic import View

from myapp.models import  User,Profile

from django.contrib import messages

from django.contrib.auth import authenticate,login

from django.core.mail import send_mail

def send_otp(user_instance):

    user_instance.generate_otp()

    send_mail(
        "django application otp",
        f"Enter the OTP  {user_instance.otp}",
        "eisondanieljohnson007gmail.com",
        [user_instance.email],
        fail_silently=False

    )

class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignUpForm()

        return render(request,"Signup.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SignUpForm(form_data)

        if form_instance.is_valid():

            user_instance=form_instance.save(commit=False)

            user_instance.is_active=False

            user_instance.save()

            send_otp(user_instance)

            return redirect("verify-otp")
        
        else:

            return render(request,"Signup.html",{"form":form_instance})



class VerifyOtpView(View):

    def get(self,request,*args,**keargs):

        return render(request,"verifyotp.html")
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        otp=form_data.get("otp")

        try:

            user_instance=User.objects.get(otp=otp)

            user_instance.is_active=True

            user_instance.is_verified=True

            user_instance.otp=None

            user_instance.save()

            messages.success(request,"Account Created Successfully")
            return redirect("signin")

        except:

            messages.error(request,"invalid Otp")

            return redirect("verify-otp")
    

class SigninView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SigninForm()

        return render(request,"Signin.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=SigninForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            
            user_instance=authenticate(request,username=uname,password=pwd)

            if user_instance:

                login(request,user_instance)

                return redirect("index")
        
        messages.error(request,"Login faild!!")
        return render(request,"Signin.html",{"form":form_instance})




class IndexView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"Index.html")
    


class ProfileEditView(View):


    def get(self,request,*args,**kwargs):

        Profile_instance=Profile.objects.get(owner=request.user)

        form_instance=UserProfileForm(instance=Profile_instance)

        return render(request,"profileEdit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        profile_instance=Profile.objects.get(owner=request.user)

        form_instance=UserProfileForm(form_data,instance=profile_instance,files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("index")
        
        else:

            return render(request,"profileEdit.html",{"form":form_instance})