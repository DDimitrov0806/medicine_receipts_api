from rest_framework.views import APIView
from rest_framework.response import Response
from receipts.serializers import PatientSerializer
from rest_framework import status
from receipts.tableModels.patientModel import Patient
from receipts.tableModels.doctorModel import Doctor
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import doctor_required, patient_required
from rest_framework.permissions import IsAuthenticated

class PatientView(APIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]

    #doctor_required
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated or not user.is_doctor:
            return Response("No permissions", status=status.HTTP_403_FORBIDDEN)
        doctors = Doctor.objects.all()
        doctor = doctors.filter(user_id=request.user.id).first()
        patients = Patient.objects.all()
        if doctor is not None:
            patients = Patient.objects.filter(doctor=doctor)
        serializer = self.serializer_class(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #patient_required
    def put(self, request, doctor_id):
        user = request.user
        if not user.is_authenticated or not user.is_patient:
            return Response("No permissions", status=status.HTTP_403_FORBIDDEN)
        doctor = Doctor.objects.filter(id=doctor_id).first()
        patient = Patient.objects.filter(user_id=request.user.id).first()
        if patient is None:
            return Response(f"Patient not found", status=status.HTTP_404_NOT_FOUND)
        
        patient.doctor=doctor
        patient.doctor_id=doctor.id
        serializer = self.serializer_class(
            patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
