"""
Import
"""
from django.shortcuts import render
from django.contrib import messages
from .models import Contact


# Create your views here.

# Contact From View


def contactForm(request):
    """
        Contact Form View
    """
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

# If the form is filled out it will save the form's content and the below
# message will be displayed

        messages.add_message(request, messages.SUCCESS,
                             'Your message had been sent!')

    return render(request, 'contact.html')
