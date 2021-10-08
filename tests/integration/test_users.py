import json
import pytest
from django.urls import reverse


from .. import factories as f

pytestmark = pytest.mark.django_db


def test_user_can_view_profile(client):
    user = f.UserFactory.create()
    client.login(user)

    url = reverse('user_retrieve_and_update')
    response = client.get(url)

    assert response.status_code == 200


def test_guest_user_cannot_view_profile(client):
    url = reverse('user_retrieve_and_update')
    response = client.get(url)
    response_data = json.loads(response.content)

    assert response.status_code == 403
    assert response_data['message'] == 'Authentication credentials were not provided.'


def test_user_can_update_profile(client):
    user = f.UserFactory.create()
    client.login(user)

    url = reverse('user_retrieve_and_update')
    data = {
        'email': 'johndoe@email.com',
        'username': 'johnnydoe',
    }

    response = client.put(url, data)
    response_data = json.loads(response.content)

    assert response.status_code == 200
    assert response_data['data']['username'] == 'johnnydoe'
