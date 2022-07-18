from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'account_number', 'balance', 'get_client_since', 'is_active')
    list_filter = ('client_id', 'is_active',)

admin.site.register(Account, AccountAdmin)
