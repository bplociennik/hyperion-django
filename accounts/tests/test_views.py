from django.contrib.auth.models import User
from django.test import TestCase

from accounts import models as accounts_models


class TestAccountList(TestCase):
    url_pattern = '/api/accounts/{filters}'

    def setUp(self):
        self.user = User.objects.create_user(
            'lennon',
            'john.lennon@gmail.com',
            'qwerty'
        )

    def test_anonymous_user(self):
        """Anonymous user should don't have access"""
        response = self.client.get(self.url_pattern.format(filters=''))
        self.assertEqual(response.status_code, 403)

    def test_authenticated_user(self):
        """Authenticated user should have access"""
        self.client.login(username=self.user.username, password='qwerty')
        response = self.client.get(self.url_pattern.format(filters=''))
        self.assertEqual(response.status_code, 200)
