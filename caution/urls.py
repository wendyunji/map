from django.urls import path
from .views import *


app_name="caution"
urlpatterns = [
    path('',caution,name="caution"),
]