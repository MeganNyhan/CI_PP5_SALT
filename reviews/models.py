# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product

# Create your models here.


class Review(models.Model):
    """
    This is the review model that allows me
    to display the reviews on the site
    """
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)