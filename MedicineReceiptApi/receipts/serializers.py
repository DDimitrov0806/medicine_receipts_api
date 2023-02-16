from rest_framework import serializers

from receipts.models import User
from .tableModels.patientModel import Patient

from .tableModels.medicineModel import Medicine
from .tableModels.pharmacyModel import Pharmacy

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields='__all__'

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name','last_name','username', 'email','adress','is_patient','is_doctor')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patient
        fields = '__all__'
        