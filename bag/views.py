from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ View the shopping bag contents """

    return render(request, 'bag.html')
