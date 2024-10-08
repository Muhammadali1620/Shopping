from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('phone_number', 'password', 'full_name')

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')

        if not phone_number:
            raise ValidationError('Phone number must be required')

        if phone_number and UserModel.objects.filter(phone_number=phone_number).exists():
            raise ValidationError({'phone_number': ['phone number is already exists']})

        return attrs

    def create(self, validated_data):
        validated_data['phone_number'] = validated_data.get('phone_number')
        return UserModel.objects.create_user(**validated_data)


class CustomUserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        password = attrs['password']

        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            raise ValidationError('password or phone number is not valid')

        token_obj, _ = Token.objects.get_or_create(user=user)
        attrs['token'] = token_obj.key

        return attrs

