from django.shortcuts import render, get_object_or_404

def mainpage(request):
    return render(request,"mainpage.html")