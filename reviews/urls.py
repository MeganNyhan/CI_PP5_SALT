from django.urls import path
from .import views

urlpatterns = [
     path('', views.reviews, name='reviews'),
     path('review_detail', views.ProductReview, name='review_detail'),
]
