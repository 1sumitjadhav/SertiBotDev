import re
import razorpay
from django.http import HttpResponse
from django.shortcuts import render


<<<<<<< HEAD
=======
from django.shortcuts import render

# from coupons.models import name



>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d
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

<<<<<<< HEAD
def success(request):
    return render(request,"Success.html")


# def Login(request):
#     return render(request,"login.html")

# def Registration(request):
#     return render(request,"signup_page.html")
 
# def welcome(request):
#     return(request,"welcome.html")

=======

def coupon(request):
    return render(request,"coupon.html")


    


# def details(request, pk):

#     owner_obj = Driver.objects.get(pk=pk)

#     car_objs = Car.objects.filter(owner_id=owner_obj.id)

#     context = {

#         "vehicles": car_objs,

#         "drivers": owner_obj,

#     }

#     return render(request, "details.html", context)
>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d
