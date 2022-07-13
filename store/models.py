from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Customer(models.Model):
    """
        Customer model
    """
    user = models.OneToOneField(User,
                                null=True, blank=True,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    """
        Order Model
    """
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    """
        Product Model
    """
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True, blank=False)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return str(self.name)



class OrderItem(models.Model):
    """
        OrderItem Model
    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    """
        Shiiping Model
    """
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                                 null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    county = models.CharField(max_length=200, null=False)
    eircode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)
