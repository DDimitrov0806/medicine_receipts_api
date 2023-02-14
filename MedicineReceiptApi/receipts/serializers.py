from rest_framework import serializers
from .models.doctorModel import  Doctor
from .models.medicineModel import Medicine
from .models.pharmacyModel import Pharmacy
from django.contrib.auth.models import User

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        #fields = ['id', 'name', 'description', 'price']
        fields='__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')