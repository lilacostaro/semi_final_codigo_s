from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from drf_yasg.utils import swagger_auto_schema


class UserRegistrationView(generics.GenericAPIView):

    serializer_class = serializers.UserRegisterSerializer

    @swagger_auto_schema(operation_summary="Register as a user of the API")
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

