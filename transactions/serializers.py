from django.contrib.auth import get_user_model
from .models import Transactions
from accounts.models import Account
from rest_framework import serializers

class MakeDepositSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    account_number = serializers.CharField(max_length=5)
    value = serializers.DecimalField(max_digits=8, decimal_places=2)  # 150.000,00
    transaction_type = serializers.CharField(default='deposito')
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Transactions
        fields = ('user_id', 'account_number', 'value', 'transaction_type', 'created_at')

    def make_deposit(self, validated_data):
        id = validated_data['account_number']
        conta = Account.objects.get(pk=id)
        current_balance = conta.balance
        new_balance = current_balance + validated_data['value']
        conta.balance = new_balance
        conta.save()

        return True

    def create(self, validated_data):
        transaction = self.make_deposit(validated_data)
        id = validated_data['account_number']
        conta = Account.objects.get(pk=id)
        user_id = conta.client_id_id
        validated_data['user_id'] = user_id
        if transaction == True:
            return super().create(validated_data)
        return {"message": "Deposito não foi efetuado"}


class MakeWithdrawSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    account_number = serializers.CharField(max_length=5)
    value = serializers.DecimalField(max_digits=8, decimal_places=2)  # 150.000,00
    transaction_type = serializers.CharField(default='saque')
    created_at = serializers.DateTimeField(read_only=True)
    token = serializers.CharField(max_length=4, write_only=True)

    class Meta:
        model = Transactions
        fields = ('user_id','account_number', 'value', 'transaction_type', 'created_at', 'token')

    def make_withdraw(self, validated_data):
        token = validated_data['token']
        id = validated_data['account_number']
        value = validated_data['value']
        conta = Account.objects.get(pk=id)
        current_balance = conta.balance
        account_token = conta.token
        if current_balance > value:
            new_balance = current_balance - value
            if account_token == token:
                conta.balance = new_balance
                conta.save()
                return True
            return {"message": "Senha Invalida"}
        return {"message": "Saldo Insuficiente"}

    def create(self, validated_data):
        transaction = self.make_withdraw(validated_data)
        id = validated_data['account_number']
        conta = Account.objects.get(pk=id)
        user_id = conta.client_id_id
        validated_data['user_id'] = user_id
        if transaction == True:
            validated_data.pop('token')
            return super().create(validated_data)
        return {"message": "Saque não foi efetuado"}


class MakeTransferSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    account_number = serializers.CharField(max_length=5)
    account_number_credit = serializers.CharField(max_length=5)
    transaction_type = serializers.CharField(default='transferencia_enviado')
    sender_token = serializers.CharField(max_length=4)
    value = serializers.DecimalField(max_digits=8, decimal_places=2)  # 150.000,00
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Transactions
        fields = ('user_id', 'account_number', 'account_number_credit', 'transaction_type',
                  'sender_token', 'value', 'created_at')

    def make_transfer(self, validated_data):
        token = validated_data['sender_token']
        id_sender = validated_data['account_number']
        id_receiver = validated_data['account_number_credit']
        value = validated_data['value']
        conta_sender = Account.objects.get(pk=id_sender)
        conta_receiver = Account.objects.get(pk=id_receiver)
        current_balance_sender = conta_sender.balance
        current_balance_receiver = conta_receiver.balance
        account_token_sender = conta_sender.token
        user_id_receiver = conta_receiver.client_id_id

        if token == account_token_sender:
            if current_balance_sender > value:
                sender_new_balance = current_balance_sender - value
                receiver_new_balance = current_balance_receiver + value
                conta_sender.balance = sender_new_balance
                conta_receiver.balance = receiver_new_balance
                trasaction_receiver = Transactions(user_id=user_id_receiver, account_number=id_receiver, value=value,
                                                   transaction_type='transferencia_recebido')

                conta_sender.save()
                conta_receiver.save()
                trasaction_receiver.save()

                return True
            return {"message": "Saldo Insuficiente"}
        return {"message": "Senha numerica invalida"}

    def create(self, validated_data):
        transfer = self.make_transfer(validated_data)
        id = validated_data['account_number']
        conta = Account.objects.get(pk=id)
        user_id = conta.client_id_id
        validated_data['user_id'] = user_id
        if transfer == True:
            validated_data.pop('account_number_credit')
            validated_data.pop('sender_token')
            return super().create(validated_data)
        return {"message": "Transferencia não foi efetuada"}


class ListTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ("account_number", "value", "transaction_type", "created_at")
