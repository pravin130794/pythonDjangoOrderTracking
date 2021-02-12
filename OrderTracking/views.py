from django.core.cache import cache
from django.shortcuts import render, redirect
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    pizza = Pizza.objects.all()
    orders = Order.objects.filter(user = request.user)
    context = {'pizza' : pizza , 'orders' : orders}
    return render(request,'index.html',context)

def details(request):
   return render(request,'details.html')


def order(request , order_id):
    if cache.get(order_id):
        print('data from Cache Redis')
        order = cache.get(order_id)
    else:
        order = Order.objects.filter(order_id=order_id).first()
        print('data from DB')
        cache.set(order_id, order)
        if order is None:
            return redirect('/')
    
    context = {'order' : order}
    return render(request , 'details.html', context)
    
@csrf_exempt
def order_pizza(request):
    user = request.user
    data = json.loads(request.body)
    
    try:
        pizza =  Pizza.objects.get(id=data.get('id'))
        order = Order(user=user, pizza=pizza , amount = pizza.price)
        order.save()
        return JsonResponse({'message': 'Success'})
        
    except Pizza.DoesNotExist:
        return JsonResponse({'error': 'Something went wrong'})