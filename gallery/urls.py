
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add-photo', views.addPhoto, name='add-photo'),
]
