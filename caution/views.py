from django.shortcuts import render
from .models import *
# Create your views here.

def caution(request):
    return render(request,'caution.html')
