from django.db import models
from django.contrib.auth import get_user_model

from core import models as core_models
from accounts.cryptography import AESCipher

User = get_user_model()


class Account(core_models.BaseDate):
    user = models.ForeignKey(User, related_name="accounts", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=255)
    login = models.CharField(max_length=64)
    _password = models.BinaryField(null=False)

    def __str__(self):
        return 'Account(id={}, user={})'.format(
            self.id,
            self.user)

    @property
    def password(self):
        return AESCipher().decrypt(self._password)

    @password.setter
    def password(self, value):
        self._password = AESCipher().encrypt(value)

    class Meta:
        ordering = ['-created_date']
