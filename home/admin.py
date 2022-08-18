from django.contrib import admin
from .models import Introduction, Profile

# Register your models here.


class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('head', 'body')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['facebook_url']


admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(Profile, ProfileAdmin)
