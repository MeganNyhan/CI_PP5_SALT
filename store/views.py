from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Customer, Product, Order, OrderItem, ShippingAddress

# Create your views here.


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, 
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
     
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, 
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        # Create an Empty cart for none logged in users:
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)

