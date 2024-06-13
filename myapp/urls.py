from django.urls import path, include
from .views import get_engine_details, get_transmission_details, DictionaryItemView

urlpatterns = [
    path('machine/<str:serial_number>/', machine_detail_by_serial, name='machine_detail_by_serial'),
    path('dictionary/model/<str:name>/', DictionaryItemView.as_view(), name='dictionary-item-model'),
    path('dictionary/engine_model/<str:name>/', get_engine_details, name='engine-details'),
    path('dictionary/transmission_model/<str:name>/', get_transmission_details, name='transmission-details'),
    path('dictionary/drive_axle_model/<str:name>/', get_drive_axle_details, name='drive-axle-details'),
    path('dictionary/steer_axle_model/<str:name>/', get_steer_axle_details, name='steer-axle-details'),
]

from django.contrib import admin

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')), 
]
