"""Imports"""
from django.db import models


class Description(models.Model):
    """Description model"""
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.name)


class Photo(models.Model):
    """Photo model"""
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return str(self.image)
