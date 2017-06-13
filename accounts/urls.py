from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()
router.register(
    prefix=r'accounts',
    base_name='accounts',
    viewset=views.AccountViewSet
)
urlpatterns = router.urls
