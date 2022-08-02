
"""Imports"""
from django.db import models
from cloudinary.models import CloudinaryField


class Description(models.Model):
    """Description model"""
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.name)


class Photo(models.Model):
    """Photo model"""
    category = models.ForeignKey(
        Description, on_delete=models.SET_NULL, null=True, blank=True)
    image = CloudinaryField(null=False, blank=False)
    information = models.TextField()

    def __str__(self):
        return str(self.information)
