import django_filters
import rest_framework.filters

from accounts import models as accounts_models


class AccountFilter(rest_framework.filters.FilterSet):
    name = django_filters.CharFilter(
        name='name',
        lookup_expr='icontains'
    )
    url = django_filters.CharFilter(
        name='url',
        lookup_expr='icontains'
    )
    login = django_filters.CharFilter(
        name='login',
        lookup_expr='icontains'
    )
    created_date = django_filters.DateFilter(
        name='created_date',
        lookup_expr='startswith'
    )
    modified_date = django_filters.DateFilter(
        name='modified_date',
        lookup_expr='startswith'
    )

    class Meta:
        model = accounts_models.Account
        fields = ['name', 'url', 'login', 'created_date', 'modified_date']
