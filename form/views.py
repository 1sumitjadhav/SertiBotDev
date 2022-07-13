from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from requests import request

# Create your views here.
from .forms import CouponForm
from coupons.models import Coupons1




def couponview(request):
    form = CouponForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CouponForm()
    context = {
        'form' : form
    }
    return render(request,"addcoupon.html",context)


    