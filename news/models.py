from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.model import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django import forms

# This tuple will keep track of drafted posts and published posts
STATUS = ((0, "Draft"), (1, "Published"))


class Profile(models.Model):
    """
        Creates User profile Model
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    """
    This is the post model that allows me
    to display the posts on the site
    """
    title = models.CharField(max_length=2000, unique=True)
    title_tag = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    snippet = models.CharField(max_length=2000, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=2000, unique=True)
    body = models.CharField(max_length=2555, unique=True)
    post_date = models.DateField(auto_add_now=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
