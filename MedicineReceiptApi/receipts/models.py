from django.db import models
from .tableModels.medicineModel import Medicine
from .tableModels.pharmacyModel import Pharmacy
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name=models.CharField(max_length=30)
    address = models.CharField(max_length=150,blank=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['address']
