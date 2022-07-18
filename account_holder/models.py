from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.
ACCOUNT_TYPE_CHOICES = [
    ('Pessoa Fisica', 'Pessoa Física'),
    ('Pessoa Júridica', 'Pessoa Júridica'),
]


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=25)
    last_name = models.CharField(_('Last name'), max_length=100)
    account_type = models.CharField(_('Account type'), max_length=15, choices=ACCOUNT_TYPE_CHOICES)
    cpf_cnpj = models.CharField(_('CPF/CNPJ'), max_length=14, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'account_type', 'cpf_cnpj']

    objects = CustomUserManager()

    def __srt__(self):
        return f'{self.first_name} {self.last_name}'


