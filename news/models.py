# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# This tuple will keep track of drafted posts and published posts
STATUS = ((0, "Draft"), (1, "Published"))

# post models for recipes section


class Post(models.Model):
    """
    This is the post model that allows me
    to display the posts on the site
    """
    title = models.CharField(max_length=2000, unique=True)
    title_tag = models.CharField(max_length=200, unique=True)
    featured_image = models.ImageField('image', default='placeholder')
    snippet = models.CharField(max_length=2000, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=2000, unique=True)
    body = models.TextField(max_length=2550, null=True,)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
