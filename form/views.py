from django.shortcuts import render

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
    context = {
        'data':data,
        'form' : form
    }
    return render(request,"addcoupon.html",context)


def couponvalidate(request):
    data = Coupons1.objects.all()
    check = request.POST.get('validate')
    status = 'invalid'
    for all in data:
        # print(all.coupons2)
        if all.coupons2 == check:
            status = 'valid'
            dell =Coupons1.objects.get(id= all.id)
            dell.delete()
    return render(request,"couponslist.html",{'data':data,'check':check,'status':status})




def coupondelet(id):
    data = Coupons1.objects.filter(id=id)
    data.delete()
    # return render(request,"couponslist.html",{'data':data})


