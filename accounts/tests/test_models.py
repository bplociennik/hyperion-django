from django.test import TestCase

from accounts import models as accounts_models

from core.tests import factories as core_factories
from accounts.tests import factories as accounts_factories


class AccountTestCase(TestCase):
    def setUp(self):
        self.password = 'simple_password'
        self.user = core_factories.UserFactory()
        self.account = accounts_factories.AccountFactory(
            user=self.user,
            password=self.password
        )

    def test_get_password(self):
        """Test password cryptography encryption"""
        account = accounts_models.Account.objects.get(
            login=self.account.login
        )

        self.assertEqual(account.password, self.password)
        self.assertNotEqual(account._password, self.password)
