from django.shortcuts import render, redirect, HttpResponse
from .models import *
# Create your views here.

def show(request):

    trenches=Trench.objects.all()

    return render(request,'map.html',{"trenches":trenches})

def ifr(request):
    return render(request,'iframemap.html')

def hi(requset):
    a=Trench.objects.all()
    for i in a:
        print(i.trench_num)
        print(i.longitude)
        print(i.latitude)
    return HttpResponse('hi') 
    