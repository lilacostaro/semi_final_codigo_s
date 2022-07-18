from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Create your models here.

User = get_user_model()

class Account(models.Model):
    client_id = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=False)
    agency = models.CharField(_('Agency'), max_length=4, default='0001')
    account_number = models.CharField(_('Account'), max_length=5, primary_key=True)
    balance = models.DecimalField(_('Balance'), max_digits=15, decimal_places=2, default=0)
    token = models.CharField(_('Token'), max_length=4)
    is_active = models.BooleanField(_('Active'), default=True)
    created_at = models.DateField(_('Cliente Since'), auto_now_add=True)
    updated_at = models.DateField(_('updated'), auto_now=True)

    class Meta:
        db_table = 'Account'

    def __str__(self):
        return f'{self.account_number}'

    def get_client_since(self):
        return self.created_at.strftime('%d-%m-%Y')