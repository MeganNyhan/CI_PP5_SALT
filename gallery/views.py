from django.shortcuts import render
from django.forms import modelformset_factory
from .models import Image
from .forms import ImageForm, ItemForm

# Create your views here.


def add_item_view(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)
    if request.method == "GET":
        item_form = ItemForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'add-item.html', {"item_form": item_form,
                                              "formset": formset})
    elif request.method == "POST":
        pass


def gallery(request):
    """ A view to return the gallery page """
    return render(request, 'gallery.html')