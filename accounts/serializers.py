from django.contrib.auth import get_user_model
from .models import Account
from rest_framework import serializers


class CreateAccountSerializer(serializers.ModelSerializer):
    agency = serializers.CharField(max_length=4, default='0001', read_only=True)
    account_number = serializers.CharField(max_length=5, read_only=True)
    balance = serializers.DecimalField(max_digits=15, decimal_places=2, default=0, read_only=True)
    token = serializers.CharField(max_length=4, write_only=True)

    class Meta:
        model = Account
        fields = ('agency', 'account_number', 'balance', 'token', 'get_client_since')

    def generate_account_number(self):
        try:
            last_account_number = Account.objects.latest('account_number').account_number
            account_number = int(last_account_number) + 1
            account_number = str(account_number)
        except:
            account_number = '1000'

        return account_number

    def create(self, validated_data):
        validated_data['account_number'] = self.generate_account_number()
        return super().create(validated_data)

# class AccountDetailSerializer(serializers.ModelSerializer):
#     agency = serializers.CharField(read_only=True)
#     account_number = serializers.CharField(read_only=True)
#     account_digit = serializers.CharField(read_only=True)
#     balance = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
#     token = serializers.CharField(max_length=4, write_only=True)
#     created_at = serializers.DateField(read_only=True)
#     updated_at = serializers.DateField(read_only=True)
#     class Meta:
#         model = Account
#         fields = ('agency', 'account_number', 'account_digit', 'balance', 'created_at', 'updated_at', 'token')
