from django.shortcuts import render

# Create your views here.


def reviews(request):
    """ A view that renders the bag contents page """

    return render(request, 'review-item.html')
