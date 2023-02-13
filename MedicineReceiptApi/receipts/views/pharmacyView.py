from rest_framework.views import APIView
from rest_framework.response import Response
from receipts.models.pharmacyModel import Pharmacy
from receipts.serializers import PharmacySerializer
from rest_framework import status


class PharmacyView(APIView):
    serializer_class = PharmacySerializer
    queryset = Pharmacy.objects.all()

    def get(self, request, id=None, *args, **kwargs):
        pharmacies = Pharmacy.objects.all()
        if id:
            pharmacies = pharmacies.filter(id=id)
        serializer = self.serializer_class(pharmacies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        req_data = {
            'name': request.data.get('name'),
            'address': request.data.get('address')
        }
        serializer = PharmacySerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        pharmacy = Pharmacy.objects.get(id=id)
        if pharmacy == None:
            return Response(f"Pharmacy with id {id} not found", status=status.HTTP_404_NOT_FOUND)
        data = {
            'name': request.data.get('name'),
            'address': request.data.get('description')
        }
        serializer = self.serializer_class(
            instance=pharmacy, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        pharmacy = Pharmacy.objects.get(id=id)
        if pharmacy == None:
            return Response(f"Pharmacy with id {id} not found", status=status.HTTP_404_NOT_FOUND)
        pharmacy.delete()
        return Response(f"Pharmacy deleted successfully", status=status.HTTP_200_OK)
