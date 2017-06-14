from django.conf.urls import url, include

from rest_framework_jwt import views as rf_jwt


urlpatterns = [
    # Remove when add frontend
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # JWT support
    url(r'^token/get/', rf_jwt.obtain_jwt_token, name='api-token-get'),
    url(r'^token/refresh/', rf_jwt.refresh_jwt_token, name='api-token-refresh'),
    url(r'^token/verify/', rf_jwt.verify_jwt_token, name='api-token-verify'),

    # Import apps
    url(r'api/', include('accounts.urls', namespace='accounts')),
    url(r'api/docs/', include('core.urls', namespace='api-docs')),
]
