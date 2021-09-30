from rest_framework import serializers

from .models import User
from .services import login


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)

    # The client should not be able to send a token along with a registration request.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        user.token = user.generate_jwt_token()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, required=True)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(
        max_length=128, write_only=True, required=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        authenticate_kwargs = {
            'email': data['email'],
            'password': data['password']
        }

        return login(**authenticate_kwargs)
