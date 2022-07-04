from django import forms  # Imports


class Contact(forms.Form):
    """
    Contact Form
    """
    name: forms.CharField(max_length=100)
    email: forms.CharField(max_length=100)
    Message: forms.CharField(max_length=2000)
