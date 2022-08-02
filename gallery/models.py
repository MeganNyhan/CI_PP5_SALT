from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Descriptions(models.Model):
    class Meta:
        verbose_name = 'Description'
        verbose_name_plural = 'Descriptions'

    user = models.Foreignkey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        return str(self.name)


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    category = models.Foreignkey(
        Descriptions, on_delete=models.SET_NULL, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()

    def __str__(self):
        return self.description
