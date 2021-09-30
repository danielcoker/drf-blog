from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

from base.mixins import SuccessMessageMixin

from .models import User
from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer


class RegistrationAPIView(SuccessMessageMixin, CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    resource_name = 'User'


class LoginAPIView(SuccessMessageMixin, APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    success_message = 'User logged in successfully.'

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(SuccessMessageMixin, RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    resource_name = 'User'

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
