from rest_framework import serializers

from receipts.models import User
from receipts.tableModels.doctorModel import Doctor
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


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        depth = 1
        
class PatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=False)

    class Meta:
        model= Patient
        fields = '__all__'
        depth = 1