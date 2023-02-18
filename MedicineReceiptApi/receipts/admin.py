from django.contrib import admin

# Register your models here.
from .tableModels.medicineModel import Medicine
from .tableModels.pharmacyModel import Pharmacy,PharmacyMedicine
from .tableModels.doctorModel import Doctor
from .tableModels.patientModel import Patient

admin.site.register(Medicine)
admin.site.register(Pharmacy)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PharmacyMedicine)