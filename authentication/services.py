from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied


def login(email: str, password: str):
    user = authenticate(username=email, password=password)

    if user is None:
        raise AuthenticationFailed(
            'Incorrect email or password.',
        )

    if not user.is_active:
        raise PermissionDenied(
            'This user has been deactivated.')

    user.token = user.generate_jwt_token()

    return user
