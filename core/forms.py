from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['created_at','status','transaction_type','category','subcategory','amount','comment']
        widgets = {
            'created_at': forms.DateInput(attrs={'type' : 'date'}),
        }    

    def clean(self):
        cleaned = super().clean()
        transaction_type = cleaned.get('transaction_type')
        category = cleaned.get('category')
        subcategory = cleaned.get('subcategory')
        if category and transaction_type and category.transcation_type.id != transaction_type.id:
            raise forms.ValidationError("Категория не соответствует выбранному типу.")
        if subcategory and category and subcategory.category_id != category.id:
            raise forms.ValidationError("Подкатегория не соответствует выбранной категории.")
        return cleaned
    