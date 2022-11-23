from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=180)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateField(auto_now=True)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    photo = models.ImageField(upload_to='image', null=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
