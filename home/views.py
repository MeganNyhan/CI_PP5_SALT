from django.shortcuts import render
from .models import Introduction, Profile
from django.template import RequestContext


# Create your views here.

# index views


def index(request):
    """ A view to return the index page """
    bodies = Introduction.objects.all()
    profile = Profile.objects.all()
    context = {'bodies': bodies, 'profile': profile}
    return render(request, 'home/index.html', context)


# faq views


def faqs(request):
    """ A view to return the index page """
    return render(request, 'home/faqs.html')


# Page 404

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
