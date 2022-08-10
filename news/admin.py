from django.contrib import admin
from news.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('head', 'body')


admin.site.register(Post, PostAdmin)
