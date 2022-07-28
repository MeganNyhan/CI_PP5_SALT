from django.shortcuts import render


# create your views here.


def wishlist(request):
    """ A view that renders the wishlist page """

    return render(request, 'wishlist.html')
