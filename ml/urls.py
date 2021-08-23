from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    #Add the following(views.py call_write_data()Allows you to send data to)
    path("ajax/", views.call_write_data, name="call_write_data"),
]