import re
import razorpay
from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
#    data={
#       'title' : 'Home Page'
#   }
    
    return render(request,"index.html")

def aboutUS(request):
    return HttpResponse("Welcome sumit")

def course(request):
    return HttpResponse("Welcome sumit course")


def userForm(request):
    return render(request,"userform.html")

def success(request):
    return render(request,"Success.html")


# def Login(request):
#     return render(request,"login.html")

# def Registration(request):
#     return render(request,"signup_page.html")
 
# def welcome(request):
#     return(request,"welcome.html")

