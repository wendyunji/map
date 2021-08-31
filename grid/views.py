from django.shortcuts import render, redirect, HttpResponse
from .models import Trench, mlResult
# Create your views here.

def show(request):

    trenches=Trench.objects.raw('select trench.trench_num, trench.longitude, trench.latitude, ml_result.acc from trench, ml_result where (trench.trench_num = ml_result.trench_num)')
    
        
    

    return render(request,'map.html',{"trenches":trenches, })

def ifr(request):
    return render(request,'iframemap.html')

def hi(requset):
    
    b=Trench.objects.extra(tables=['ml_result'], where=['trench.trench_num = ml_result.trench_num']).all()
    a= Trench.objects.raw('select trench.trench_num, trench.longitude, trench.latitude, ml_result.acc from trench, ml_result where (trench.trench_num = ml_result.trench_num)')
    print(a.query)

    for x in a:
        print(x.trench_num)
        print(x.acc) 
    return HttpResponse('hi')
    