from django.urls import path
from .views import *


app_name="grid"
urlpatterns = [
    path('',show,name="show"),
    path('ifr/',ifr,name="ifr"),
    path('hi/',hi,name="hi"),
]