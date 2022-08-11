from django import forms
from .models import Product, Category, Review


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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)

# Review Form 

class ReviewForm(forms.ModelForm):
    """
        This is the Review Form for the Products
    """
    class Meta:
        model = Review
        fields = ('name', 'body')
    # Widget section
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
