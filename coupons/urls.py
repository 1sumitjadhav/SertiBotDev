from django.contrib import admin
from django.db import router
from django.urls import path , include
from . import views


# from rest_framework import routers       
# router = routers.DefaultRouter()
# router.register(r'api/' ,  basename='Coupons1')  

urlpatterns = [
    path('',views.getData),
    path('add/',views.additem),
]
