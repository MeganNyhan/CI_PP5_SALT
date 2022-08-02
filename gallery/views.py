from django.shortcuts import render
from .models import Description, Photo
# Create your views here.


def gallery(request):
    """ A view to return the index page """
    categories = Description.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)


def addPhoto(request):
    """ A view to return the index page """
    return render(request, 'add-photo.html')
