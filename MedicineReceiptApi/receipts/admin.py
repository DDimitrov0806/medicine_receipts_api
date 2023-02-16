from django.contrib import admin

# Register your models here.
from .tableModels.medicineModel import Medicine
from .tableModels.pharmacyModel import Pharmacy

admin.site.register(Medicine)
admin.site.register(Pharmacy)