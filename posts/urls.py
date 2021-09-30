from django.urls import path

from .views import PostListCreateAPIView

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='post_list_create'),
]
