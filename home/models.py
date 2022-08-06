from django.db import models

# Create your models here.
"""
imports from Django.
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

# This tuple will keep track of drafted posts and published posts
STATUS = ((0, "Draft"), (1, "Published"))


class Profile(models.Model):
    """ 
        Creates User Profile Model
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField('image', default='placeholder')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Introduction(models.Model):
    """ Changes the text in the home page header """
    head = models.CharField(max_length=300, null=True, blank=True)
    body = models.TextField(max_length=2550, null=True, blank=True)
