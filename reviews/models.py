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
    user = models.ForeignKey(User, related_name='reviews',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
