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
