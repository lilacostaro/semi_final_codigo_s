from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Transactions
from accounts.models import Account
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class MakeDepositView(generics.GenericAPIView):
    serializer_class = serializers.MakeDepositSerializer
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Allows you to make deposits on your account.")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MakeWithdrawView(generics.GenericAPIView):
    serializer_class = serializers.MakeWithdrawSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Allows you to make withdraws on your account.")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        user = request.user
        user_id = user
        account_id = data.get('account_number')
        user_account_id = Account.objects.get(pk=account_id).client_id

        if serializer.is_valid():
            if user_account_id == user_id:
                serializer.save()

                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": "Saque não autorizado. Só o titular da conta pode realizar saques"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MakeTransferView(generics.GenericAPIView):
    serializer_class = serializers.MakeTransferSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Allows you to make a transfer of your account to another account.")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        user = request.user
        user_id = user
        account_id = data.get('account_number')
        user_account_id = Account.objects.get(pk=account_id).client_id

        if serializer.is_valid():
            if user_account_id == user_id:
                serializer.save()

                return Response({"message": "Transferencia Realizada"}, status=status.HTTP_201_CREATED)
            return Response({"message": "Transferencia não autorizada. Só o titular da conta pode realizar transferencias."},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListAllTransactionsView(generics.GenericAPIView):
    serializer_class = serializers.ListTransactionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Gets you the historical view of your account transactions.")
    def get(self, request):
        user = request.user
        all_transactions = Transactions.objects.filter(user_id=user.id)
        print(all_transactions)
        serializer = self.serializer_class(instance=all_transactions, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ListLastWeekTransactionsView(generics.GenericAPIView):
    serializer_class = serializers.ListTransactionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Gets you all your accounts transactions in the last week.")
    def get(self, request):
        last_week = datetime.now() - timedelta(days=7)
        user = request.user
        all_transactions = Transactions.objects.filter(user_id=user.id, created_at__gt=last_week)
        print(all_transactions)
        serializer = self.serializer_class(instance=all_transactions, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ListLastMonthTransactionsView(generics.GenericAPIView):
    serializer_class = serializers.ListTransactionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Gets you all your accounts transactions in the last month.")
    def get(self, request):
        last_week = datetime.now() - timedelta(days=30)
        user = request.user
        all_transactions = Transactions.objects.filter(user_id=user.id, created_at__gt=last_week)
        print(all_transactions)
        serializer = self.serializer_class(instance=all_transactions, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ListLastTrimesterTransactionsView(generics.GenericAPIView):
    serializer_class = serializers.ListTransactionSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Gets you all your accounts transactions in the last trimester.")
    def get(self, request):
        last_week = datetime.now() - timedelta(days=90)
        user = request.user
        all_transactions = Transactions.objects.filter(user_id=user.id, created_at__gt=last_week)
        print(all_transactions)
        serializer = self.serializer_class(instance=all_transactions, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

