from django.contrib import admin
from contact.models import Contact

# register Models


class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'Message')


admin.site.register(Contact, ContactAdmin)
