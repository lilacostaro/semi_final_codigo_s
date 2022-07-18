from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Account
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

class CreateAccountView(generics.GenericAPIView):
    serializer_class = serializers.CreateAccountSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Return all information about your account. You can check your balance here.")
    def get(self, request):
        user = request.user
        accounts = Account.objects.get(client_id=user)
        serializer = self.serializer_class(instance=accounts)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Allows you to create an account by setting a for digits token that will be used to authenticate your transactions.")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        user = request.user

        if serializer.is_valid():
            serializer.save(client_id=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AccountDetailView(generics.GenericAPIView):
#
#     serializer_class = serializers.AccountDetailSerializer
#
#     def get(self, request, account_id):
#         account = get_object_or_404(Account, pk=account_id)
#         serializer = self.serializer_class(instance=account)
#
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, account_id):
#         pass
#
#     def delete(self, request, account_id):
#         pass
