from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializes regitration requests and creates a new uesr.
    """

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and cannot be read by the client.
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
