from django.db import models

# Create your models here.
"""
    imports
"""
from django.db import models


# Create your models here.
class Contact(models.Model):
    """
        Contact Model for contact section of site
    """
    name = models.CharField(max_length=150, blank=False, null=True)
    email = models.EmailField(default='DEFAULT VALUE', blank=True, null=True)
    message = models.CharField(max_length=1500, blank=False, null=True)

    def __str__(self):
        return str(self.email)