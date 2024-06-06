from rest_framework import routers
from .views import MachineViewSet, MaintenanceViewSet, ComplaintViewSet

router = routers.DefaultRouter()
router.register(r'machines', MachineViewSet)
router.register(r'maintenances', MaintenanceViewSet)
router.register(r'complaints', ComplaintViewSet)

urlpatterns = router.urls
