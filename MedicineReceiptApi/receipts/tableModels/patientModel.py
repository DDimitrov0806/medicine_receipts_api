from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from receipts.tableModels.doctorModel import Doctor


class Patient(models.Model):
    pin = models.CharField(max_length=10, blank=False, validators=[MinLengthValidator(10)])
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="personal_doctor")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'patient'