from django.urls import path

from .views import UserRetrieveUpdateAPIView

urlpatterns = [
    path('', UserRetrieveUpdateAPIView.as_view(),
         name='user_retrieve_and_update')
]
