from django.contrib import admin
from .models import Item, Image


# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
