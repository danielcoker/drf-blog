from django.urls import path

from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('', UserRetrieveUpdateAPIView.as_view(),
         name='user_retrieve_and_update'),
    path('/login', LoginAPIView.as_view(), name='users_login'),
    path('/register', RegistrationAPIView.as_view(),
         name='authentication_register')
]
