from django.shortcuts import render, get_object_or_404, redirect
from .models import Review


# Create your views here.


def reviews(request):
    """ A view that renders the bag contents page """

    return render(request, 'review-item.html')


def ProductReview(request):
    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating', '')
        content = request.POST.get('content', '')
        review = ProductReview.objects.create(product=product, user=request.user, rating=rating, content=content)

        return redirect('product_detail',  product_id=product_id)
