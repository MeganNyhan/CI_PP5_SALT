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


class OrderItem(models.Model):
    """
        Order Item Model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL,
        blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL,
        blank=True, null=True)
    payment = models.ForeignKey(
        'payment', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    recieved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total