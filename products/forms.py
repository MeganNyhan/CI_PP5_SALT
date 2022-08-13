from django import forms
from .models import Product, Category, ProductComment

# product form


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black '


# review form


# To add a comment feature:
# copied and modified from
# https://djangocentral.com/creating-comments-system-with-django/,
# Abhijeet Pal, Author and Editor in Chief @djangocentral,
# on August 13th, 2022.
class ProductCommentForm(forms.ModelForm):
    """
    Class for the product comment form
    """
    class Meta:
        model = ProductComment
        fields = ('body', 'rating')
