"""Imports"""
from django.db import models

# Description Model


class Description(models.Model):
    """Description model"""
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)


# Photo Model


class Photo(models.Model):
    """Photo model"""

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    category = models.ForeignKey(
        Description, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.image)
