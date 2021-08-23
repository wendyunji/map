from django.shortcuts import redirect, render, get_object_or_404

def mainpage(request):
    return render(request,"mainpage.html")


def test():
    return redirect("/test")