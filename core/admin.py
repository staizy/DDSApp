from django.contrib import admin
from .models import Status, TransactionType, Category, Subcategory, Transaction

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','transcation_type')
    list_filter = ('transcation_type',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name','category')
    list_filter = ('category',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('created_at','status','transaction_type','category','subcategory','amount',)
    list_filter = ('transaction_type','status','category','subcategory','created_at',)
    search_fields = ('comment',)