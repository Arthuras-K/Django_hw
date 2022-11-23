from django.urls import path
from .views import SensorsView, SensorOneView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorOneView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
