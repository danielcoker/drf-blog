from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from base.mixins import SuccessMessageMixin

from .serializers import RegistrationSerializer


class RegistrationAPIView(SuccessMessageMixin, CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    resource_name = 'User'
