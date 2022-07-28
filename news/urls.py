# import views
from django.urls import path
from .views import NewsView, PostDetailView, UpdatePostView, DeletePostView


urlpatterns = [
    path('news-list/', NewsView.as_view(), name='news-list'),
    path('article/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
]
