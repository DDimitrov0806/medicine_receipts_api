from rest_framework import serializers
from receipts.models import Receipt
 
 
class ReceiptSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Receipt
        fields = ['id','name','description','price']