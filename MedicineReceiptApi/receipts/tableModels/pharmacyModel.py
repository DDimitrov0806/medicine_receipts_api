from django.db import models
from .medicineModel import Medicine

class Pharmacy(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    address = models.CharField(max_length=200, blank=False, default='')
    medicines = models.ManyToManyField(Medicine, through='PharmacyMedicine',blank=True, null=True)

    class Meta:
        db_table = 'pharmacy'

class PharmacyMedicine(models.Model):
    medicine= models.ForeignKey(Medicine,on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('pharmacy','medicine')