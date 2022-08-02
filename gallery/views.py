from django.shortcuts import render
# Create your views here.


def gallery(request):
    """ A view to return the index page """
    return render(request, 'gallery.html')


def addPhoto(request):
    """ A view to return the index page """
    return render(request, 'add-photo.html')