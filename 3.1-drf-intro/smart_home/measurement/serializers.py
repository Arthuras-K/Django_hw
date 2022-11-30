from rest_framework import serializers
from .models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'photo']


class MeasurementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id_sensor', 'temperature', 'created_at', 'photo']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']