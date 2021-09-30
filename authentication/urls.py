from django.urls import path

from .views import LoginAPIView, RegistrationAPIView

urlpatterns = [
    path('/login', LoginAPIView.as_view(), name='users_login'),
    path('/register', RegistrationAPIView.as_view(),
         name='authentication_register')
]
