from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MachineViewSet, MaintenanceViewSet, ComplaintViewSet, machine_detail_by_serial, DictionaryItemView, get_engine_details, get_transmission_details, get_drive_axle_details, get_steer_axle_details, get_maintenance_type_details, get_organization_details, get_service_company_details, get_failure_node_details, get_recovery_method_details

router = DefaultRouter()
router.register(r'machines', MachineViewSet)
router.register(r'maintenances', MaintenanceViewSet)
router.register(r'complaints', ComplaintViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('machine/<str:serial_number>/', machine_detail_by_serial, name='machine_detail_by_serial'),
    path('dictionary/model/<str:name>/', DictionaryItemView.as_view(), name='dictionary-item-model'),
    path('dictionary/engine_model/<str:name>/', get_engine_details, name='engine-details'),
    path('dictionary/transmission_model/<str:name>/', get_transmission_details, name='transmission-details'),
    path('dictionary/drive_axle_model/<str:name>/', get_drive_axle_details, name='drive-axle-details'),
    path('dictionary/steer_axle_model/<str:name>/', get_steer_axle_details, name='steer-axle-details'),
    path('dictionary/maintenance_type/<str:name>/', get_maintenance_type_details, name='maintenance-type-details'),
    path('dictionary/organization/<str:name>/', get_organization_details, name='organization-details'),
    path('dictionary/service_company/<str:name>/', get_service_company_details, name='service-company-details'),
    path('dictionary/failure_node/<str:name>/', get_failure_node_details, name='failure-node-details'),
    path('dictionary/recovery_method/<str:name>/', get_recovery_method_details, name='recovery-method-details'),
]











