from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email','username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    username = serializers.CharField(required=True,
                                     validators=[UniqueValidator(queryset=User.objects.all(),
                                                                 message="That username is already in use.")])
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all(),
                                                               message="That email is already in use.")])
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('dob', 'sex', 'about', 'user')
