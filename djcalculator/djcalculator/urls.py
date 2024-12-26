"""
URL configuration for djcalculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operation.views import AdditionView
from operation.views import SubtractionView
from operation.views import MultiplicationView
from operation.views import VehichleRegistrationView
from operation.views import SingUpView
from  operation.views import AppointmentRequestFormView
from  operation.views import BmiFormView
from  operation.views import MilageFormView
from  operation.views import EmiFormView,CalorieFormView,IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("add/",AdditionView.as_view(),name="add"),
    path("sub/",SubtractionView.as_view(),name="sub"),
    path("multi/",MultiplicationView.as_view(),name="multi"),
    path("vehicle/",VehichleRegistrationView.as_view(),name="vehicle"),
    path("Signup/",SingUpView.as_view(),name="signup"),
    path("application/",AppointmentRequestFormView.as_view(),name="app"),
    path("bmi/",BmiFormView.as_view(),name="bmi"),
    path("milage/",MilageFormView.as_view(),name="milage"),
    path("emi/",EmiFormView.as_view(),name="emi"),
    path("calorie/",CalorieFormView.as_view(),name="calorie"),
    path("",IndexView.as_view(),name="index"),

    
    
    ]