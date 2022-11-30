from django.urls import path
from .views import SensorsView, SensorOneView, MeasurementView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorOneView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurement/', MeasurementCreateView.as_view()),
]
