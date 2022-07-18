from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Account
from django.utils.translation import gettext_lazy as _

User = get_user_model()

TRANSACTIONS_TYPE_CHOICES = (
    ('saque', 'saque'),
    ('deposito', 'deposito'),
    ('transferencia_enviado', 'transferencia_enviado'),
    ('transferencia_recebido', 'transferencia_recebido'),
)
# 22

class Transactions(models.Model):
    user_id = models.IntegerField()
    account_number = models.CharField(max_length=5)
    value = models.DecimalField(max_digits=8, decimal_places=2) # 150.000,00
    transaction_type = models.CharField(max_length=22, choices=TRANSACTIONS_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


