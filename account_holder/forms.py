from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from pyexpat import model

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'account_type', 'cpf_cnpj')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'account_type', 'cpf_cnpj')