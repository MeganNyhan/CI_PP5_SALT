"""
Imports
"""

from django.db import models

# Contact Model


class Contact(models.Model):
    """
    Contact Model for the contact from of site
    """
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.CharField(default='DEFUALT VALUE', max_length=200, blank=False, null=True)
    message = models.CharField(max_length=2000, blank=False, null=True)

    def __str__(self):
        return str(self.email)
