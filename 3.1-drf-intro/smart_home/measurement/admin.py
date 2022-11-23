from django.contrib import admin
from .models import Measurement, Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
