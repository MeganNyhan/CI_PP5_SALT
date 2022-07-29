from django.contrib import admin
from .models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['id', 'user', 'product', 'rate', 'created_at']
    readonly_fields = ['created_at']