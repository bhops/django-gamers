from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserProfile

class UserCreateSerializer(serializers.ModelSerializer):

    def validate_email(self, data):
        if User.objects.filter(email=data):
            raise serializers.ValidationError('email taken')

    def validate_username(self, data):
        if User.objects.filter(username=data):
            raise serializers.ValidationError('username taken')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email','username', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email','username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('dob', 'sex', 'about', 'user')
