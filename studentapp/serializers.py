from studentapp.models import *
from rest_framework import serializers
from django.contrib.auth import login,authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        attrs['user'] = user
        return attrs


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField()
    class Meta:
        model=Student
        fields="__all__"