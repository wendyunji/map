from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
# application/write_data.Import py
from .application import write_data

# Create your views here.
def index(req):
    return render(req, 'index.html')

#Method specified by url with ajax
def call_write_data(req):
    if req.method == 'GET':
        # write_data.py write_csv()Call the method.
        #Of the data sent by ajax"input_data"To get by specifying.
        write_data.write_csv(req.GET.get("input_data"))
        return HttpResponse()