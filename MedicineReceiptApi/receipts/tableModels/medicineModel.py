from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=300, blank=True, default='')

    class Meta:
        db_table = 'medicine'
