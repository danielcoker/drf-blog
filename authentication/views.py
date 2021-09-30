from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from base.mixins import SuccessMessageMixin

from .serializers import LoginSerializer, RegistrationSerializer


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
