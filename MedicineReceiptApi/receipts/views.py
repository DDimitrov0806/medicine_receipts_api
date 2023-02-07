from rest_framework import generics
from receipts.models import ReceiptModel
from receipts.serializer import ReceiptSerializer
from django.http.response import JsonResponse
from rest_framework import status

class Receipts(generics.GenericAPIView):
    serializer_class = ReceiptSerializer
    queryset = ReceiptModel.objects.all()
    
    def get(self, request, request_id):
        if request_id!=None:
            receipt = ReceiptModel.objects.get(id=request_id)
            serializer = self.serializer_class(receipt, data=request.data)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        filter_id = request.GET.get("id")
        receipts = ReceiptModel.objects.all()
        if id:
            receipts.filter(id=filter_id)
        serialize = self.serializer_class(receipts,many=True)
        return JsonResponse(serialize.data, safe=False)

    def post(self, request,request_id):
        receipt = ReceiptModel.objects.get(id=request_id)
        if receipt == None:
            return JsonResponse(f"Receipt with id {request_id} not found",status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(receipt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, request_id):
        receipt = ReceiptModel.objects.get(id=request_id)
        if receipt == None:
            return JsonResponse(f"Receipt with id {request_id} not found",status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(receipt,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, request_id):
        receipt = ReceiptModel.objects.get(id = request_id)
        if receipt == None:
            return JsonResponse(f"Receipt with id {request_id} not found",status=status.HTTP_404_NOT_FOUND)
        receipt.delete()
        return JsonResponse(f"Receipt deleted successfully",status=status.HTTP_200_OK)