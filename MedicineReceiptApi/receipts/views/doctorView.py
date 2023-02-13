from rest_framework.views import APIView
from rest_framework.response import Response
from receipts.models.doctorModel import Doctor
from receipts.serializers import DoctorSerializer
from rest_framework import status


class DoctorView(APIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    def get(self, request, id=None, *args, **kwargs):
        doctors = Doctor.objects.all()
        if id:
            doctors = doctors.filter(id=id)
        serializer = self.serializer_class(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        req_data = {
            'name': request.data.get('name'),
            'address': request.data.get('address')
        }
        serializer = DoctorSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        receipt = Doctor.objects.get(id=id)
        if receipt == None:
            return Response(f"Doctor with id {id} not found", status=status.HTTP_404_NOT_FOUND)
        data = {
            'name': request.data.get('name'),
            'address': request.data.get('description')
        }
        serializer = self.serializer_class(
            instance=receipt, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        receipt = Doctor.objects.get(id=id)
        if receipt == None:
            return Response(f"Doctor with id {id} not found", status=status.HTTP_404_NOT_FOUND)
        receipt.delete()
        return Response(f"Doctor deleted successfully", status=status.HTTP_200_OK)
