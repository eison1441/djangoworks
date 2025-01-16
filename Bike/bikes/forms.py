from django import forms
from bikes.models import Bike
from django.contrib.auth.models import User


# class BikeAddForm(forms.Form):

#     name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
#     brand=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
#     fuel_choice=(
#         ("petrol","Petrol"),
#         ("diesel","Diesel")
#     )
#     fuel_type=forms.ChoiceField(choices=fuel_choice,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))
#     color=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
#     mileage=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
#     image=forms.ImageField()
    

class BikeAddForm(forms.ModelForm):

    class Meta:

        model=Bike

        fields="__all__"

        widgets={

            "name":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "brand":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "price":forms.NumberInput(attrs={"class":"form-control mb-3"}),
            "fuel_type":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "color":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "mileage":forms.NumberInput(attrs={"class":"form-control mb-3"}),
            "image":forms.FileInput(attrs={"class":"form-control mb-3"}),
        }

class BikeSignUpForm(forms.ModelForm):
    
    class Meta:

        model=User

        fields=["username","email","first_name","last_name","password"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control mb-3 "}),
            "email":forms.EmailInput(attrs={"class":"form-control mb-3 "}),
            "first_name":forms.TextInput(attrs={"class":"form-control mb-3 "}),
            "last_name":forms.TextInput(attrs={"class":"form-control mb-3 "}),
            "password":forms.PasswordInput(attrs={"class":"form-control mb-3 "}),

        }


class BikeSignInForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mb-3 text-primary", "style": "color: #f8f9fa;"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control mb-3 text-primary", "style": "color: #f8f9fa;"}))
