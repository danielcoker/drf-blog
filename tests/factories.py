import factory


class Factory(factory.django.DjangoModelFactory):
    pass


class UserFactory(Factory):
    class Meta:
        model = 'authentication.User'

    username = factory.Sequence(lambda n: 'user{}'.format(n))
    email = factory.LazyAttribute(lambda obj: '%s@email.com' % obj.username)
    password = factory.PostGeneration(
        lambda obj, *args, **kwargs: obj.set_password(obj.username))


class PostFactory(Factory):
    class Meta:
        model = 'posts.Post'

    title = factory.Sequence(lambda n: 'Post {}'.format(n))
    body = factory.Sequence(lambda n: 'Post {} body.'.format(n))
    author = factory.SubFactory('tests.factories.UserFactory')
    is_active = True


class CommentFactory(Factory):
    class Meta:
        model = 'posts.Comment'

    body = factory.Sequence(lambda n: 'Comment {}'.format(n))
    post = factory.SubFactory('tests.factories.PostFactory')
    author = factory.SubFactory('tests.factories.UserFactory')
