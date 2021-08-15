from django.shortcuts import render, redirect, HttpResponse
from .models import *
# Create your views here.

def show(request):
    return render(request,'map.html')

def ifr(request):
    return render(request,'iframemap.html')

def hi(requset):
    a=Trench.objects.all()
    for i in a:
        print(i.trench_num)
    return HttpResponse('hi') 
    