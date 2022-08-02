from django.urls import path
from . import views


urlpatterns = [
    path('gallery', views.gallery, name="gallery"),
    path('add-item', views.add_item_view, name="add-item"),
]
