from django.shortcuts import render

# Create your views here.
from django.conf.urls import url 
from coupons import views 

from rest_framework.response import Response

from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'nm':'ds','nmgfdg':24}
    return Response(person)
