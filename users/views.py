from django.shortcuts import get_object_or_404, render, redirect
from .models import *
# Create your views here.

def mypage(request):
    user=request.user

    return render(request,"users/mypage.html",{"user":user})

def edit(request):  # 개인만 쓸 페이지
    user = request.user
    return render(request, "users/edit.html", {"user": user})


def update(request):  # 개인만 쓸 함수
    update_profile = request.user.profile
    update_profile.tonnage = request.POST["tonnage"]
    update_profile.ship = request.POST["ship"]
    update_profile.active_sea = request.POST["active_sea"]
    update_profile.save()

    return redirect("users:introduce")