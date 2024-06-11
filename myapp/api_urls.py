# api_urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineViewSet, MaintenanceViewSet, ComplaintViewSet, machine_detail_by_serial, DictionaryItemView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'machines', MachineViewSet)
router.register(r'maintenances', MaintenanceViewSet)
router.register(r'complaints', ComplaintViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('machine/<str:serial_number>/', machine_detail_by_serial, name='machine_detail_by_serial'),
    path('dictionary/<int:id>/', DictionaryItemView.as_view(), name='dictionary-item'),  # Измените здесь
]








