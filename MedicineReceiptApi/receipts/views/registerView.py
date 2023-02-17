from rest_framework import generics, permissions
from receipts.models import User
from receipts.tableModels.patientModel import Patient
from receipts.tableModels.doctorModel import Doctor
from receipts.serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        first_name = request.data.get("firstName")
        last_name = request.data.get("lastName")
        address = request.data.get("address")
        email = request.data.get("email")
        password = request.data.get("password")
        pin = request.data.get("pin")
        specialty = request.data.get("specialty")
        role = request.data.get("role")
        
        is_patient = role == 'patient'
        is_doctor = role == 'doctor'

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User(username=email,first_name=first_name,last_name=last_name, email=email, address=address, password=password,is_doctor=is_doctor,is_patient=is_patient,is_staff=True,is_superuser=False)
        user.set_password(password)

        user.save()
        if is_patient:
            patient = Patient.objects.create(pin=pin,user=user)
        if is_doctor:
            doctor = Doctor.objects.create(specialty=specialty, user=user)
        return Response({"message": "User registered successfully"},status=status.HTTP_200_OK)