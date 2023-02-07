from rest_framework import serializers
from receipts.models import ReceiptModel
 
 
class ReceiptSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ReceiptModel
        fields = '__all__'