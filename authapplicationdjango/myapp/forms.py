from django import forms

from myapp.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
       
       model=User

       fields=["username","email","password1","password2","phone"]

       widgets={
           
              "username":forms.TextInput(attrs={"class":"form-control"}),
    
              "email":forms.EmailInput(attrs={"class":"form-control"}),
    
              "password1":forms.PasswordInput(attrs={"class":"form-control"}),
    
              "password2":forms.PasswordInput(attrs={"class":"form-control"}),
    
              "phone":forms.TextInput(attrs={"class":"form-control"}),

       }