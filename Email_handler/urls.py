from django.urls import path, include
from . import views
urlpatterns = [
    path('checkdata/',views.checkdata,name='checkdata')
]