from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    address = models.CharField(max_length=200, blank=False, default='')

    class Meta:
        db_table = 'doctor'
