from django.db import models
from members.models import UserProfile

# Create your models here.


# category model for products

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name


# product model for products

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=3000)
    description = models.TextField()
    size = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    instock = models.BooleanField(default=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField('image', default='placeholder')

    def __str__(self):
        return str(self.name)


# Product review model for products

class ProductComment(models.Model):
    # Review Custom Model
    # To add a comment feature:
    # copied and modified
    # from https://djangocentral.com/creating-comments-system-with-django/,
    # Abhijeet Pal, Author and Editor in Chief @djangocentral,
    # on August 14th, 2022.

    """
    Django Product Comment Model
    """
    class Meta:
        ordering = ['created_on']

    # To limit field content to specific values,
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/,
    # accessed on August 14th, 2022.

    user = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
