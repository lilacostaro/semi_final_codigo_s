from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    User = get_user_model()
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=25)
    last_name = serializers.CharField(max_length=100)
    account_type = serializers.CharField(max_length=15)
    cpf_cnpj = serializers.CharField(min_length=11, max_length=14, write_only=True)
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)


    class Meta:
        User = get_user_model()
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'account_type', 'cpf_cnpj')

    def validate(self, attrs):
        email_exists = self.User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail='User with this email already exists')

        cpf_cnpj_exists = self.User.objects.filter(cpf_cnpj=attrs['cpf_cnpj']).exists()

        if cpf_cnpj_exists:
            raise serializers.ValidationError(detail='User with this cpf/cnpj already exists')

        return super().validate(attrs)

    def create(self, validated_data):
        return self.User.objects.create_user(**validated_data)
