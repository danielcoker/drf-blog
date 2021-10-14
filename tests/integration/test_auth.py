import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


@pytest.fixture
def register_payload():
    return {
        'email': 'johndoe@email.com',
        'username': 'johndoe',
        'password': 'Password321',
    }


@pytest.fixture
def register_endpoint():
    return reverse('auth-register')


def test_respond_201_after_registration(client, register_endpoint, register_payload):
    response = client.post(register_endpoint, register_payload)
    assert response.status_code == 201


def test_respond_400_if_required_fields_are_empty(client, register_endpoint):
    response = client.post(register_endpoint, {})
    assert response.status_code == 400


def test_respond_400_if_username_or_email_is_duplicate(client, register_endpoint, register_payload):
    response = client.post(register_endpoint, register_payload)
    assert response.status_code == 201

    response = client.post(register_endpoint, register_payload)
    assert response.status_code == 400


def test_user_login_with_correct_credentials(client, register_endpoint, register_payload):
    response = client.post(register_endpoint, register_payload)

    login_payload = {
        'email': register_payload['email'],
        'password': register_payload['password']
    }

    response = client.post(reverse('auth-login'), login_payload)
    assert response.status_code == 200


def test_login_with_incorrect_credentials(client, register_endpoint, register_payload):
    register_payload['email'] = 'valid_email@email.com'
    register_payload['password'] = 'valid_password'

    response = client.post(register_endpoint, register_payload)

    login_payload = {
        'email': 'invalid_email@email.com',
        'password': 'valid_password',
    }

    response = client.post(reverse('auth-login'), login_payload)
    assert response.status_code == 403

    login_payload = {
        'email': 'valid_email@email.com',
        'password': 'invalid_password',
    }

    response = client.post(reverse('auth-login'), login_payload)
    assert response.status_code == 403
