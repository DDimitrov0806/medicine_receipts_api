from django.contrib import admin

# Register your models here.
from .models.medicineModel import Medicine
from .models.doctorModel import Doctor
from .models.pharmacyModel import Pharmacy

admin.site.register(Medicine)
admin.site.register(Doctor)
admin.site.register(Pharmacy)