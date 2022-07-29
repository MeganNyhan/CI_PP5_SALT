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
    user = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    comment = models.TextField(max_length=250, blank=False)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
