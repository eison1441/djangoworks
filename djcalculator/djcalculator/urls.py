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
from  operation.views import EmiFormView,CalorieFormView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("add/",AdditionView.as_view()),
    path("sub/",SubtractionView.as_view()),
    path("multi/",MultiplicationView.as_view()),
    path("vehicle/",VehichleRegistrationView.as_view()),
    path("Signup/",SingUpView.as_view()),
    path("application/",AppointmentRequestFormView.as_view()),
    path("bmi/",BmiFormView.as_view()),
    path("milage/",MilageFormView.as_view()),
    path("emi/",EmiFormView.as_view()),
    path("calorie/",CalorieFormView.as_view()),

    
    
    ]