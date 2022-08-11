from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name


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


class Review(models.Model):
    # Review Custom Model
    post = models.ForeignKey(Product, on_delete=models.CASCADE,
                             related_name="reviews")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)

    class Meta:
        # Ordering
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"

