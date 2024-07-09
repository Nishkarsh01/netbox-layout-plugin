# api/urls.py
from netbox.api.routers import NetBoxRouter
from .views import RackAreaViewSet

router = NetBoxRouter()
router.register('rack-areas', RackAreaViewSet)

urlpatterns = router.urls
