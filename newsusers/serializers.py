from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            password=make_password(validated_data.get('password')),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'avatar',)
