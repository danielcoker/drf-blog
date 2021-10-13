import json
from random import randint
import pytest
from django.urls import reverse

from posts.models import Post


from .. import factories as f

pytestmark = pytest.mark.django_db


def test_create_post(client):
    user = f.UserFactory.create()
    url = reverse('posts-list')
    data = {'title': 'Post Name', 'body': 'Post body.'}

    client.login(user)
    response = client.post(url, data)
    response_data = json.loads(response.content)['data']

    assert response.status_code == 201
    assert response_data['title'] == data['title']
    assert response_data['body'] == data['body']


def test_list_posts(client):
    post3 = f.PostFactory.create(title='Post Test 3', body='Post body 3.')
    post2 = f.PostFactory.create(title='Post Test 2', body='Post body 2.')
    post1 = f.PostFactory.create(title='Post Test 1', body='Post body 1.')

    url = reverse('posts-list')

    response = client.get(url)
    response_data = json.loads(response.content)['data']

    assert response.status_code == 200
    assert response_data[0]['id'] == post1.id
    assert response_data[1]['id'] == post2.id
    assert response_data[2]['id'] == post3.id


def test_get_post_detail(client):
    post = f.PostFactory.create()

    url = reverse('posts-detail', kwargs={'pk': post.id})

    response = client.get(url)
    response_data = json.loads(response.content)['data']

    assert response.status_code == 200
    assert response_data['id'] == post.id


def test_get_post_details_with_non_existent_id(client):
    post = f.PostFactory.create()

    url = reverse('posts-detail',
                  kwargs={'pk': randint(1000, 2000)})

    client.login(post.author)
    response = client.get(url)

    assert response.status_code == 404


def test_update_post(client):
    post = f.PostFactory.create()
    data = {'title': 'Update Post Title', 'body': 'Update post body.'}

    url = reverse('posts-detail', kwargs={'pk': post.id})

    client.login(post.author)
    response = client.put(url, data)
    response_data = json.loads(response.content)['data']

    assert response.status_code == 200
    assert response_data['id'] == post.id
    assert response_data['title'] == data['title']
    assert response_data['body'] == data['body']


def test_update_post_with_non_existent_id(client):
    user = f.UserFactory.create()
    data = {'title': 'Update Post Title', 'body': 'Update post body.'}

    url = reverse('posts-detail',
                  kwargs={'pk': randint(1000, 2000)})

    client.login(user)
    response = client.put(url, data)

    assert response.status_code == 404


def test_update_post_for_another_author(client):
    user = f.UserFactory.create()
    post = f.PostFactory.create()
    data = {'title': 'Update Post Title', 'body': 'Update post body.'}

    url = reverse('posts-detail', kwargs={'pk': post.id})

    client.login(user)
    response = client.put(url, data)

    assert response.status_code == 403


def test_delete_post(client):
    post = f.PostFactory.create()

    url = reverse('posts-detail', kwargs={'pk': post.id})

    client.login(post.author)
    response = client.delete(url)

    assert response.status_code == 204
    assert Post.objects.filter(id=post.id).count() == 0


def test_delete_post_with_non_existent_id(client):
    user = f.UserFactory.create()
    url = reverse('posts-detail',
                  kwargs={'pk': randint(1000, 2000)})

    client.login(user)
    response = client.delete(url)

    assert response.status_code == 404


def test_delete_post_for_another_author(client):
    user = f.UserFactory.create()
    post = f.PostFactory.create()

    url = reverse('posts-detail', kwargs={'pk': post.id})

    client.login(user)
    response = client.delete(url)

    assert response.status_code == 403


############################
# Comments Endpoints
############################
def test_create_comment_for_post(client):
    user = f.UserFactory.create()
    post = f.PostFactory.create()
    data = {'body': 'Test comment for a post.'}

    url = reverse('post-comments-list', kwargs={'post_id': post.id})

    client.login(user)
    response = client.post(url, data)

    assert response.status_code == 201
