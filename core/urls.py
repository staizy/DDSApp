from django.urls import path
from . import views

app_name = 'core' 

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='transaction_list'),
    path('create/', views.TransactionCreateView.as_view(), name='transaction_create'),
    path('edit/<int:pk>/', views.TransactionUpdateView.as_view(), name='transaction_edit'),
    path('delete/<int:pk>/', views.TransactionDeleteView.as_view(), name='transaction_delete'),

]
