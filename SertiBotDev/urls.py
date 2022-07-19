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
from django.urls import path, include
<<<<<<< HEAD
# from accounts.views import Login

from .import views






=======
from SertiBotDev import views
from login.views import loginaction
from signup.views import signupaction
>>>>>>> 142aa82c495c613cdb0428c501344417a6ad6dc4

urlpatterns = [
    path('',views.homePage),
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutUS),
    path('course/',views.course),
    # path('welcome/',views.welcome,name='welcome'),
    path('userform/',views.userForm, name="userform"),
<<<<<<< HEAD
    path('accounts/',include('accounts.urls')),
    
    
=======
    path('email/',include('Email_handler.urls')),
    path('login/',loginaction),
    path('signup',signupaction),
>>>>>>> 142aa82c495c613cdb0428c501344417a6ad6dc4
]
