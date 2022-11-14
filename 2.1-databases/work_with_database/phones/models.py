from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.CharField(max_length=256)
    release_date = models.CharField(max_length=10)
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=50)
