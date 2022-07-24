
import random
import string
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from coupons.models import Coupons1 
from coupons import views 

from rest_framework.response import Response
from rest_framework.decorators import api_view


# @api_view(['GET'])
# def getData(request):
#     # person = {'nm':'ds','nmgfdg':24}
#     items = Coupons1.objects.all()
#     serializer = serializers.CouponsSerializer(items, many= True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def additem(request):
#     serializer = serializers.CouponsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response()



# Create your views here.

from django.shortcuts import render
from requests import request

# Create your views here.
from .forms import CouponForm
from coupons.models import Coupons1




def couponview(request):
    data = Coupons1.objects.all()
    form = CouponForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CouponForm()    
        # return HttpResponseRedirect(reverse("views.couponview"))


    bulk= request.POST.get('bulk')
    if bulk != None:
        itn=int(bulk)
        for i in range(itn):
            cp=''.join(random.choice(string.ascii_letters) for x in range(6))
            Coupons1(coupons2 =cp ,discount=random.randint(25,60),valid_for=random.randint(25,60)).save()
            
    context = {
        'data':data,
        'form' : form
    }
    return render(request,"addcoupon.html",context)


def couponvalidate(request):
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        print("User is not logged in :()")
        return redirect('/')
    
    data = Coupons1.objects.all()
    check = request.POST.get('validate')
    status = 'invalid'
    for all in data:
        # print(all.coupons2)
        if all.coupons2 == check:
            status = 'valid'
            dell =Coupons1.objects.get(id= all.id)
            dell.delete()
            return redirect('/tool')

    
    return render(request,"couponsvalidate.html",{'data':data,'check':check,'status':status})




def coupondelet(id):
    data = Coupons1.objects.filter(id=id)
    data.delete()
    # return render(request,"couponsvalidate.html",{'data':data})


