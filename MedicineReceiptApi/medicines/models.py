from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=300, blank=True, default='')
    price = models.FloatField(blank=False, default=0.0)

    class Meta:
        db_table='medicine'
