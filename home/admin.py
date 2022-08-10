from django.contrib import admin
from .models import Introduction

# Register your models here.


class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('head', 'body')


admin.site.register(Introduction, IntroductionAdmin)
