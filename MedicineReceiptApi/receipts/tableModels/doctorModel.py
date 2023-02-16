from django.db import models
from django.conf import settings

class Doctor(models.Model):
    specialty = models.CharField(max_length=50,blank=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'doctor'