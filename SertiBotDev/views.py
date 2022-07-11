import imp
from django.http import HttpResponse
from django.shortcuts import render


from django.shortcuts import render

# from coupons.models import name



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
