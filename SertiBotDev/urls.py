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
<<<<<<< HEAD
from django.urls import path, include

from accounts.views import success
# from accounts.views import Login

from .import views





=======
<<<<<<< HEAD
from django.db import router
from django.urls import path , include
from coupons.views import couponvalidate


from coupons.views import couponview
from . import views

=======
from django.urls import path, include
from accounts.views import index


>>>>>>> main
>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('about-us/',views.aboutUS),
    path('course/',views.course),
    # path('welcome/',views.welcome,name='welcome'),
    path('userform/',views.userForm, name="userform"),
<<<<<<< HEAD
    path('accounts/',include('accounts.urls')),
    path('success',views.success,name='success')
    
=======
    # path('coupons/',include('coupons.urls')),
    path('add/',couponview),
    path('list/',couponvalidate),
=======
    path('', index ,name='index'),
    path('accounts/',include('accounts.urls')),
    path('gen',include('Email_handler.urls')),

    
>>>>>>> main
>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d
    
]
