from django.contrib import admin
from .models import Transactions

# Register your models here.
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'account_number', 'value', 'transaction_type', 'created_at')
    list_filter = ('user_id', 'account_number',)

admin.site.register(Transactions, TransactionsAdmin)
