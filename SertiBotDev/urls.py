"""SertiBotDev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.db import router
from django.urls import path , include

# from SertiBotDev.coupons.models import Coupons1
# from SertiBotDev.coupons.viewsets import Couponsviewset
from . import views
from .router import router


# from rest_framework import routers       
# router = routers.DefaultRouter()
# router.register(r'api/' ,  basename='Coupons1')  

urlpatterns = [
    path('',views.homePage),
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutUS),
    path('course/',views.course),
    path('userform/',views.userForm, name="userform"),
    path('api/',include(router.urls)),
    path('test/',include('coupons.urls')),
    # path('<int:pk>/',views.details),
    # path('details/',views.details),
    
]
