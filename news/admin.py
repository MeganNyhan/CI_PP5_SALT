from django.contrib import admin
from news.models import Post, Comment

# Register your models here.
# register Models
admin.site.register(Post)
admin.site.register(Comment)
