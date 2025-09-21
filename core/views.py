from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Transaction, Status, TransactionType, Category, Subcategory
from .forms import TransactionForm

class TransactionListView(ListView):
    model = Transaction
    template_name = 'core/transaction_list.html'
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset()
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        status = self.request.GET.get('status')
        transaction_type = self.request.GET.get('transaction_type')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')

        if date_from:
            qs = qs.filter(created_at__gte=date_from)
        if date_to:
            qs = qs.filter(created_at__lte=date_to)
        if status:
            qs = qs.filter(status_id=status)
        if transaction_type:
            qs = qs.filter(transaction_type_id=transaction_type)
        if category:
            qs = qs.filter(category_id=category)
        if subcategory:
            qs = qs.filter(subcategory_id=subcategory)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['transaction_types'] = TransactionType.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        return context

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'core/transaction_form.html'
    success_url = reverse_lazy('core:transaction_list')

    def form_valid(self, form):
        form.instance.full_clean()
        return super().form_valid(form)

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'core/transaction_form.html'
    success_url = reverse_lazy('core:transaction_list')

    def form_valid(self, form):
        form.instance.full_clean()
        return super().form_valid(form)

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'core/transaction_confirm_delete.html'
    success_url = reverse_lazy('core:transaction_list')

