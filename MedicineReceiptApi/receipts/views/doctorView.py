from rest_framework.views import APIView
from rest_framework.response import Response
from receipts.serializers import DoctorSerializer
from rest_framework import status
from receipts.tableModels.patientModel import Patient
from receipts.tableModels.doctorModel import Doctor
from rest_framework.permissions import IsAuthenticated


class DoctorView(APIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated or not user.is_patient:
            return Response("No permissions", status=status.HTTP_403_FORBIDDEN)
        doctors = Doctor.objects.all()
        doctor = None
        patient = Patient.objects.filter(user_id=request.user.id).first()
        if patient is not None and patient.doctor_id is not None:
            doctor = Doctor.objects.filter(id=patient.doctor_id).first()
        if doctor is not None:
            doctors = [doctor]
        serializer = self.serializer_class(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
