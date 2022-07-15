from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField

CATEGORY_CHOICES = (
    ('P', 'Plain Sea Salt'),
    ('F', 'Flavoured Sea Salt'),
    ('H', 'Himalayan Salt')
)

# Create your models here.


class UserProfile(models.Model):
    """
        User Profile Model
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    """
        Item Model
    """
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField()
    description = models.TextField()
    image = CloudinaryField()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_to_cart_url(self):
        return reverse("core:remove-to-cart", kwargs={
            'slug': self.slug
        })