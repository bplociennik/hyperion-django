from rest_framework import serializers as rf_serializers

from accounts import models as accounts_models


class AccountSerializer(rf_serializers.ModelSerializer):
    password = rf_serializers.CharField()

    class Meta:
        model = accounts_models.Account
        fields = ('id', 'name', 'url', 'login', 'password', 'created_date', 'modified_date')
