import factory

from core.tests import factories as core_factories


class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'accounts.Account'

    user = factory.SubFactory(core_factories.UserFactory)
    name = factory.Sequence(lambda n: 'name{nb}'.format(nb=n))
    login = factory.Sequence(lambda n: 'login%s' % n)
    url = factory.LazyAttribute(lambda o: 'https://%s.com' % o.login)
    password = 'qwerty'
