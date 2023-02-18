from rest_framework.views import APIView
from rest_framework.response import Response
from receipts.tableModels.pharmacyModel import PharmacyMedicine
from receipts.serializers import PharmacyMedicineSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..tableModels.pharmacyModel import Pharmacy
from ..tableModels.medicineModel import Medicine
from ..tableModels.pharmacyModel import Pharmacy


class PharmacyMedicineView(APIView):
    serializer_class = PharmacyMedicineSerializer
    queryset = PharmacyMedicine.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pharmacies = Pharmacy.objects.prefetch_related('medicines').all()

        data = []
        for pharmacy in pharmacies:
            for medicine in pharmacy.medicines.all():
                data.append({
                    'pharmacy_id': pharmacy.id,
                    'pharmacy_name': pharmacy.name,
                    'pharmacy_address': pharmacy.address,
                    'medicine_name': medicine.name,
                    'medicine_description': medicine.description,
                    'medicine_price': pharmacy.medicines.through.objects.get(medicine=medicine, pharmacy=pharmacy).price,
                })

            # If the pharmacy has no medicines, include it in the response with null medicine fields
            if not pharmacy.medicines.exists():
                data.append({
                    'pharmacy_id': pharmacy.id,
                    'pharmacy_name': pharmacy.name,
                    'pharmacy_address': pharmacy.address,
                    'medicine_name': None,
                    'medicine_description': None,
                    'medicine_price': None,
                })

        return Response(data, status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        medicine_id = request.data.get('medicine_id')
        pharmacy_id = request.data.get('pharmacy_id')
        price = request.data.get('price')

        medicine = Medicine.objects.filter(id=medicine_id).first()
        pharmacy = Pharmacy.objects.filter(id=pharmacy_id).first()

        pharmacy_medicine = PharmacyMedicine.objects.create(pharmacy=pharmacy, medicine=medicine, price=price)
        
        serializer = PharmacyMedicineSerializer(pharmacy_medicine)

        return Response(serializer.data,status=status.HTTP_201_CREATED)
