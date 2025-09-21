from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
    def validate(self, data):
        if data['category'].transaction_type_id != data['txn_type'].id:
            raise serializers.ValidationError("Категория не относится к типу")
        if data['subcategory'].category_id != data['category'].id:
            raise serializers.ValidationError("Подкатегория не относится к категории")
        return data
