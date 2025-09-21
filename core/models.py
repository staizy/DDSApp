from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import datetime

class Status(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class TransactionType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    transcation_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, related_name="categories")
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Transaction(models.Model):
    created_at = models.DateField(default=datetime.date.today)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='transactions')
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='transactions')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    comment = models.TextField(blank=True, null=True)

    class Meta:
         ordering = ['-created_at']

    def __str__(self):
        return f"{self.date} | {self.transaction_type} | {self.amount} ₽"
    def clean(self):
        if self.category.transcation_type_id != self.transaction_type_id:
            raise ValidationError("Выбранная категория не относится к выбранному типу.")
        if self.subcategory.category_id != self.category_id:
            raise ValidationError("Выбранная подкатегория не относится к выбранной категории.")