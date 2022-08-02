
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
]


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def faqs(request):
    """ A view to return the index page """
    return render(request, 'home/faqs.html')