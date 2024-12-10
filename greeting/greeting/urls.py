"""
URL configuration for greeting project.

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
from myapp.views import HelloworldView
from myapp.views import GoodmorningView
from myapp.views import GoodafternoonView
from myapp.views import GoodnightView
from myapp.views import GoodeveningView
from myapp.views import MohanlalViwe
from myapp.views import MammoottyViwe
from myapp.views import RobertDowneyJrView
from myapp.views import KamalHaasanView
from myapp.views import RajinikanthView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Helloworld/",HelloworldView.as_view()),
    path("morning/",GoodmorningView.as_view()),
    path("night/",GoodnightView.as_view()),
    path("afternoon/",GoodafternoonView.as_view()),
    path("goodevening/",GoodeveningView.as_view()),
    path("mohanlal/",MohanlalViwe.as_view()),
    path("mammootty/",MammoottyViwe.as_view()),
    path("rdj/",RobertDowneyJrView.as_view()),
    path("kamal/",KamalHaasanView.as_view()),
    path("Rejini/",RajinikanthView.as_view()),
    

]
