from http.client import HTTPResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from receipts.models import Receipt
from receipts.serializer import ReceiptSerializer
from django.http.response import JsonResponse
from rest_framework import status

class ReceiptView(APIView):
    serializer_class = ReceiptSerializer
    queryset = Receipt.objects.all()
    
    # def get_all(self,request, *args, **kwargs):
    #     receipts = Receipt.objects.all()
    #     serializer = ReceiptSerializer(receipts,many=True)
    #     #return JsonResponse(receipts, status=status.HTTP_200_OK)
    #     #return HTTPResponse(receipts)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, id=None, *args, **kwargs):
        #request_id = request.data.get('id')
        receipts = Receipt.objects.all()
        if id:
            receipts = receipts.filter(id=id)
        serializer = self.serializer_class(receipts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args,**kwargs):
        req_data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'price': request.data.get('price')
        }
        serializer = ReceiptSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def put(self,request, id):
        receipt = Receipt.objects.get(id=id)
        if receipt == None:
            return Response(f"Receipt with id {id} not found",status=status.HTTP_404_NOT_FOUND)
        data = {
            'name': request.data.get('name'), 
            'description': request.data.get('description'), 
            'price': request.data.get('price')
        }
        serializer = self.serializer_class(instance = receipt,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        receipt = Receipt.objects.get(id=id)
        if receipt == None:
            return Response(f"Receipt with id {id} not found",status=status.HTTP_404_NOT_FOUND)
        receipt.delete()
        return Response(f"Receipt deleted successfully",status=status.HTTP_200_OK)