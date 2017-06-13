# import faker
# import factory
# import factory.django
#
# from accounts import models as accounts_models
#
# fkr = faker.Faker()
#
#
# class AccountFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = 'accounts.Account'
#
#     user = factory.SubFactory(OrganizationAdminUserFactory)
#     name = factory.Sequence(lambda n: 'name{nb}'.format(nb=n))
#     url = 'https://google.com/'
#     login = 'login'
#     _password = 'qwerty'
