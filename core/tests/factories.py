import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'auth.User'

    username = factory.Sequence(lambda n: 'lennon%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@hyperion.com' % o.username)
    password = factory.PostGenerationMethodCall('set_password', username)
