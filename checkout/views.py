from django.shortcuts import render, redirect, reverse
from django.contrib import messages 

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LNgPyHWsQMSnRqidTEUvmUFEdtnB66WhoWDNCOfbGmsCAPYWGSJZ6I13X0Zp9jte9SgnFHlqjaOfpVWxKuIJXTk003zyWhZJn',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
