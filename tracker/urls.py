from django.urls import path
from .views import RegisterDeviceView, SubmitLocationView, LocationHistoryView, DeviceListView

urlpatterns = [
    path('devices/register/', RegisterDeviceView.as_view()),
    path('locations/', SubmitLocationView.as_view()),
    path('locations/<str:device_id>/', LocationHistoryView.as_view()),
    path('devices/', DeviceListView.as_view()),
]
