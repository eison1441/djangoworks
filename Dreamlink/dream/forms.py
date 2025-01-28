from django import forms

from dream.models import User

from django.contrib.auth.forms import UserCreationForm

from dream.models import Profile

class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mb-3 mt-3 text-info","placeholder":"Enter Password"}),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mb-3 mt-3 text-info","placeholder":"Conform Password"}),
        label="Confirm Password"
    )
    class Meta:
       
       
       model=User

       fields=["username","email","password1","password2","phone"]

       widgets={
           
              "username":forms.TextInput(attrs={"class":"form-control  mt-3 mb-3 text-info","placeholder":"Enter Username"}),
    
              "email":forms.EmailInput(attrs={"class":"form-control  mt-3 mb-3 text-info","placeholder":"Enter email"}),
    
             
    
              "phone":forms.TextInput(attrs={"class":"form-control  mt-3 mb-3 text-info","placeholder":"Enter Phone Number"}),

       }

class SignInForm(forms.Form):

#     username=forms.CharField(widget={forms.TextInput(attrs={"class":"form-control mt-3 "})})
#     password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mt-3"}))

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mb-3 text-primary"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control mb-3 text-primary"}))



class UserProfileForm(forms.ModelForm):

    class Meta:

        model=Profile

        exclude=("owner",)

        widgets={
           
              "address":forms.Textarea(attrs={"class":"form-control mt-3 rounded-4 text-info"}),
    
              "bio":forms.TextInput(attrs={"class":"form-control mt-3 rounded-4 text-info"}),
    
              "picture":forms.FileInput(attrs={"class":"form-control mt-3 rounded-4 text-info"}),

       }
