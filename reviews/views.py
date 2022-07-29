from django.shortcuts import render, get_object_or_404
from .models import Review


# Create your views here.


def reviews(request):
    """ A view that renders the bag contents page """

    return render(request, 'review-item.html')


def review_list(request):
    latest_review_list = Review.objects.order_by('created_at')
    context = {'latest_review_list': latest_review_list}
    return render(request, 'review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_details.html', {'review': review})
