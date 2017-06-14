import json
import urllib.parse

from django.test import TestCase

from core.tests import factories as core_factories
from accounts.tests import factories as accounts_factories
from accounts import models as accounts_models


class TestAccountListView(TestCase):
    url_pattern = '/api/accounts/?{filters}'

    def setUp(self):
        self.user = core_factories.UserFactory()

    def test_anonymous_user(self):
        """Anonymous user should don't have access"""
        response = self.client.get(self.url_pattern.format(filters=''))
        self.assertEqual(response.status_code, 403)

    def test_authenticated_user(self):
        """Authenticated user should have access"""
        self.client.force_login(self.user)
        response = self.client.get(self.url_pattern.format(filters=''))
        self.assertEqual(response.status_code, 200)

    def test_account_filter_by_name(self):
        """Accounts filter by name"""
        self.client.force_login(self.user)

        account = accounts_factories.AccountFactory(
            user=self.user,
            name='Google'
        )

        filters = urllib.parse.urlencode({
            'name': account.name[:3]
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['name'], account.name)
        self.assertEqual(len(response.data['results']), 1)

    def test_account_filter_by_url(self):
        """Accounts filter by url"""
        self.client.force_login(self.user)

        account = accounts_factories.AccountFactory(
            user=self.user,
            url='http://google.com/'
        )

        filters = urllib.parse.urlencode({
            'url': account.url[:10]
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['url'], account.url)
        self.assertEqual(len(response.data['results']), 1)

    def test_account_filter_by_login(self):
        """Accounts filter by login"""
        self.client.force_login(self.user)

        account = accounts_factories.AccountFactory(
            user=self.user,
            login='spartacus'
        )

        filters = urllib.parse.urlencode({
            'login': account.login[:5]
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['login'], account.login)
        self.assertEqual(len(response.data['results']), 1)

    def test_account_filter_by_created_date(self):
        """Accounts filter by created date"""
        self.client.force_login(self.user)

        account = accounts_factories.AccountFactory(
            user=self.user
        )

        filters = urllib.parse.urlencode({
            'created_date': str(account.created_date)[:10]
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['created_date'], account.created_date.isoformat())
        self.assertEqual(len(response.data['results']), 1)

    def test_account_filter_by_modified_date(self):
        """Accounts filter by modified date"""
        self.client.force_login(self.user)

        account = accounts_factories.AccountFactory(
            user=self.user
        )

        filters = urllib.parse.urlencode({
            'modified_date': str(account.modified_date)[:10]
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][0]['modified_date'], account.modified_date.isoformat())
        self.assertEqual(len(response.data['results']), 1)

    def test_sort_by_name(self):
        """Accounts sort by name"""
        self.client.force_login(self.user)

        for i in range(0, 4):
            accounts_factories.AccountFactory(
                user=self.user
            )

        filters = urllib.parse.urlencode({
            'ordering': 'name'
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        ordered_accounts = accounts_models.Account.objects.order_by('name')
        for result, account in zip(response.data['results'], ordered_accounts):
            self.assertEqual(result['name'], account.name)

    def test_sort_by_url(self):
        """Accounts sort by url"""
        self.client.force_login(self.user)

        for i in range(0, 4):
            accounts_factories.AccountFactory(
                user=self.user
            )

        filters = urllib.parse.urlencode({
            'ordering': '-url'
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        ordered_accounts = accounts_models.Account.objects.order_by('-url')
        for result, account in zip(response.data['results'], ordered_accounts):
            self.assertEqual(result['url'], account.url)

    def test_sort_by_login(self):
        """Accounts sort by login"""
        self.client.force_login(self.user)

        for i in range(0, 4):
            accounts_factories.AccountFactory(
                user=self.user
            )

        filters = urllib.parse.urlencode({
            'ordering': 'login'
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        ordered_accounts = accounts_models.Account.objects.order_by('login')
        for result, account in zip(response.data['results'], ordered_accounts):
            self.assertEqual(result['login'], account.login)

    def test_sort_by_created_date(self):
        """Accounts sort by created date"""
        self.client.force_login(self.user)

        for i in range(0, 4):
            accounts_factories.AccountFactory(
                user=self.user
            )

        filters = urllib.parse.urlencode({
            'ordering': 'created_date'
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        ordered_accounts = accounts_models.Account.objects.order_by('created_date')
        for result, account in zip(response.data['results'], ordered_accounts):
            self.assertEqual(result['created_date'], account.created_date.isoformat())

    def test_sort_by_modified_date(self):
        """Accounts sort by modified date"""
        self.client.force_login(self.user)

        for i in range(0, 4):
            accounts_factories.AccountFactory(
                user=self.user
            )

        filters = urllib.parse.urlencode({
            'ordering': '-modified_date'
        })

        url = self.url_pattern.format(filters=filters)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        ordered_accounts = accounts_models.Account.objects.order_by('-modified_date')
        for result, account in zip(response.data['results'], ordered_accounts):
            self.assertEqual(result['modified_date'], account.modified_date.isoformat())

    def test_create_account_as_authenticated_user(self):
        """Create new account using post method as authenticated user"""
        self.client.force_login(self.user)

        data = {
            'name': 'Google account',
            'url': 'https://google.com',
            'login': 'lennon',
            'password': 'lennon123'
        }

        url = self.url_pattern.format(filters='')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['url'], data['url'])
        self.assertEqual(response.data['login'], data['login'])
        self.assertEqual(response.data['password'], data['password'])

    def test_create_account_as_anonymous_user(self):
        """Create new account using post method as anonymous user"""
        data = {
            'name': 'Google account',
            'url': 'https://google.com',
            'login': 'lennon',
            'password': 'lennon123'
        }

        url = self.url_pattern.format(filters='')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 403)


class TestAccountDetailView(TestCase):
    url_pattern = '/api/accounts/{id}/'

    def setUp(self):
        self.user = core_factories.UserFactory()

        self.account = accounts_factories.AccountFactory(
            user=self.user,
            login='lennon',
            password='lennon123'
        )

    def test_anonymous_user(self):
        """Anonymous user should don't have access"""
        response = self.client.get(self.url_pattern.format(id=self.account.id))
        self.assertEqual(response.status_code, 403)

    def test_authenticated_user(self):
        """Authenticated user should have access"""
        self.client.force_login(self.user)
        response = self.client.get(self.url_pattern.format(id=self.account.id))
        self.assertEqual(response.status_code, 200)

    def test_update_account(self):
        """Test update account action"""
        self.client.force_login(self.user)

        data = {
            'login': 'spartacus',
            'password': 'qwerty'
        }

        url = self.url_pattern.format(id=self.account.id)
        response = self.client.patch(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['login'], data['login'])
        self.assertEqual(response.data['password'], data['password'])

    def test_delete_account(self):
        """Test delete account action"""
        self.client.force_login(self.user)

        account = accounts_factories.AccountFactory(
            user=self.user
        )

        url = self.url_pattern.format(id=account.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(accounts_models.Account.objects.filter(id=account.id).exists())
