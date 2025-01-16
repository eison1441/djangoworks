from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from myapp.models import Expense



class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mb-3"}),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mb-3"}),
        label="Confirm Password"
    )


    class Meta:

        model=User

        fields=["username","email","password1","password2"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control mb-3 "}),
            "email":forms.EmailInput(attrs={"class":"form-control mb-3 "}),
            # "password1":forms.PasswordInput(attrs={"class":"form-control mb-3 "}),
            # "password2":forms.PasswordInput(attrs={"class":"form-control mb-3 "}),
            
        }


class SignInForm(forms.Form):
     
     username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
     password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))


class ExpenseForm(forms.ModelForm):

    # title=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
    # amount=forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control mb-3"}))

    class Meta:

        model=Expense

        exclude=("created_at","owner")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "amount":forms.NumberInput(attrs={"class":"form-control mb-3"}),
            "category":forms.Select(attrs={"class":"form-control  form-select"}),
            
            
        }

def __str__(self):
        
        return self.title

