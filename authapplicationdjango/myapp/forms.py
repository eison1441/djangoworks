from django import forms

from myapp.models import User
from myapp.models import Profile


from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control  rounded-4 mb-3"}),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control  rounded-4 mb-3"}),
        label="Confirm Password"
    )
    class Meta:
       
       
       model=User

       fields=["username","email","password1","password2","phone"]

       widgets={
           
              "username":forms.TextInput(attrs={"class":"form-control mt-3 rounded-4"}),
    
              "email":forms.EmailInput(attrs={"class":"form-control mt-3 rounded-4"}),
    
             
    
              "phone":forms.TextInput(attrs={"class":"form-control mt-3 rounded-4"}),

       }


class SigninForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mt-1  mb-2 rounded-4"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control mt-1 rounded-4 mb-2"}),label="Password")


class UserProfileForm(forms.ModelForm):

    class Meta:

        model=Profile

        exclude=("owner",)

        widgets={
           
              "address":forms.Textarea(attrs={"class":"form-control mt-3 rounded-4 text-info"}),
    
              "bio":forms.TextInput(attrs={"class":"form-control mt-3 rounded-4 text-info"}),
    
              "picture":forms.FileInput(attrs={"class":"form-control mt-3 rounded-4 text-info"}),

       }
