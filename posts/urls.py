from django.urls import path

from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('/<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view(),
         name='post_retrieve_update_destroy'),
    path('', PostListCreateAPIView.as_view(), name='post_list_create'),
]
