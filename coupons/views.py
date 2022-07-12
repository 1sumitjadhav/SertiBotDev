from django.shortcuts import render

# Create your views here.
from django.conf.urls import url
from coupons import serializers
from coupons.models import Coupons1 
from coupons import views 

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    # person = {'nm':'ds','nmgfdg':24}
    items = Coupons1.objects.all()
    serializer = serializers.CouponsSerializer(items, many= True)
    return Response(serializer.data)


@api_view(['POST'])
def additem(request):
    serializer = serializers.CouponsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()


