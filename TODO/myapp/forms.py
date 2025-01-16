from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from myapp.models import Todo




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
        }

class SignInForm(forms.Form):

#     username=forms.CharField(widget={forms.TextInput(attrs={"class":"form-control mt-3 "})})
#     password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mt-3"}))

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mb-3 text-primary"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control mb-3 text-primary"}))






class AddProjectForm(forms.ModelForm):

    class Meta:

        model = Todo

        exclude=("created_at","owner")

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control mb-3"}),
            
            
            "status":forms.Select(attrs={"class":"form-control mb-3 form-select"}),

            "due_date": forms.DateInput(attrs={'class': 'form-control mb-3' ,'type': 'date' ,}),

            
            "category":forms.Select(attrs={"class":"form-control mb-3 form-select"}),

            "priority":forms.Select(attrs={"class":"form-control mb-3 form-select"}),

        }






def __str__(self):
    return self.title