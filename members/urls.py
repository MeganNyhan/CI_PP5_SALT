from django.urls import path
from .views import User


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('register/', UserRegisterView.as_view(), name="register"),
]       