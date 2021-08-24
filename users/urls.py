from django.urls import path
from .views import *


app_name="users"
urlpatterns = [
    path("mypage/",mypage,name="mypage"),
    path("myinfo/",myinfo,name="myinfo"),
    path("edit/",edit,name="edit"),
    path("update/",update,name="update"),
    path("introduce/", introduce, name="introduce"),

]