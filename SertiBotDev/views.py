import imp
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.shortcuts import render


def homePage(request):
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
        return redirect('tool/')
    else:
        print("User is not logged in :()")
    return render(request,"index.html")

def aboutUS(request):
    return HttpResponse("Welcome sumit")

def course(request):
    return HttpResponse("Welcome sumit course")


def userForm(request):
    return render(request,"userform.html")


def coupon(request):
    return render(request,"coupon.html")



def tool(request):
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        print("User is not logged in :()")
        return redirect('/')
    return render(request,"tool.html")
    


