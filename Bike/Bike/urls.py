"""
URL configuration for Bike project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from bikes.views import BikeAddView,BikeListView,BikeDetailsView,BikeDeleteView,BikeUpdateView,BikeSignUpView,BikeSignInView,IndexView,SignOutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Bike/add/",BikeAddView.as_view(),name="Bike_add"),
    path("Bike/all/",BikeListView.as_view(),name="Bike_list"),
    path("Bike/<int:pk>/",BikeDetailsView.as_view(),name="Bike_details"),
    path("bikes/<int:pk>/remove",BikeDeleteView.as_view(),name="Bike_delete"),
    path("bikes/<int:pk>/chande/",BikeUpdateView.as_view(),name="Bike_update"),
    path("bikeregister/",BikeSignUpView.as_view(),name="register"),
    path("bikesignin/",BikeSignInView.as_view(),name="signin"),
    path("index/",IndexView.as_view(),name="index"),
    path("signout/",SignOutView.as_view(),name="signout"),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
