from django import forms
from .models import Item, Image


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', )


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )