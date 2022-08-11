from django.shortcuts import render
from .models import Description, Photo


# Gallery View

def gallery(request):
    """ A view to return the index page """
    categories = Description.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)

# addPhoto View


def addPhoto(request):
    """ A view to return the index page """
    categories = Description.objects.all()
    context = {'categories': categories}
    return render(request, 'add-photo.html', context)
