import rest_framework.permissions
import rest_framework.viewsets
import rest_framework.generics
import rest_framework.response
import rest_framework.status
import rest_framework.filters

from accounts import serializers as accounts_serializers
from accounts import filtering as accounts_filtering


class AccountViewSet(rest_framework.viewsets.ModelViewSet):
    """
    API Endpoints using Account model
    
    retrieve:
    Return account object.
    
    list:
    Return a list of all accounts for logged user.
    
    create:
    Create a new account assigned logged user.
    
    update:
    Logged user can update account data.
    
    delete:
    Delete account object.
    
    """
    serializer_class = accounts_serializers.AccountSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)

    filter_backends = (
        rest_framework.filters.OrderingFilter,
        rest_framework.filters.DjangoFilterBackend
    )

    filter_class = accounts_filtering.AccountFilter

    ordering_fields = ('id', 'name', 'url', 'login', 'created_date', 'modified_date')

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )

    def get_queryset(self):
        return self.request.user.accounts.all()
