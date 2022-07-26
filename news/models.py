# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

# This tuple will keep track of drafted posts and published posts
STATUS = ((0, "Draft"), (1, "Published"))


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
    body = models.TextField(max_length=2550, null=True,)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    
class Comment(models.Model):
    """
    This comment model will allow me to post a comment under the
    posts.
    """
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
