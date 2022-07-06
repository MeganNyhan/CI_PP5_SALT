""" 
    Imports
"""
from django import forms
from .models import Post

class EditForm(forms.ModelForm):
    """
        This is the EDIT form
    """
    class Meta:
        model = Post
        fields = ('title', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'This is the Title Input'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'This is the News Snippet Input'}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'This is the News Body Input'}),
                                             
        }
