from django.shortcuts import render
from .models import Introduction

# Create your views here.


def index(request):
    """ A view to return the index page """
    bodies = Introduction.objects.all()
    context = {'bodies': bodies}
    return render(request, 'home/index.html', context)


def faqs(request):
    """ A view to return the index page """
    return render(request, 'home/faqs.html')
