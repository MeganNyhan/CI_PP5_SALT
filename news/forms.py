""" 
    Imports
"""
from django import forms
from .models import Post, Comment

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


class CommentForm(forms.ModelForm):
    """
        This is the Comment Form for the news storys
    """
    class Meta:
        model = Comment
        fields = ('name', 'body')
    # Widget section
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
