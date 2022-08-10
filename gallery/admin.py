from django.contrib import admin
from .models import Description, Photo


# Register your models here.
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('name')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'image', 'category')


admin.site.register(Description, DescriptionAdmin)
admin.site.register(Photo, PhotoAdmin)
