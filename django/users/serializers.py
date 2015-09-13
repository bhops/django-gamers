from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True,
                                     validators=[UniqueValidator(queryset=User.objects.all(),
                                                                 message="That username is already in use.")])
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all(),
                                                               message="That email is already in use.")])
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name','email')
        write_only_fields = ('password',)
        read_only_fields = ('id', 'username',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('dob', 'sex', 'about', 'user')
