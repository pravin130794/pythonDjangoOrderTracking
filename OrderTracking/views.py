
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('Order Tracking')
    return render(request,'index.html')

def details(request):
    return HttpResponse('Order  details')