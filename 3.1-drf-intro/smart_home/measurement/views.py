from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Measurement, Sensor
from .serializers import SensorDetailSerializer, MeasurementSerializer, MeasurementCreateSerializer, SensorSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorOneView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
