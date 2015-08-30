from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    about = serializers.CharField(source='userprofile.about')
    sex = serializers.CharField(source='userprofile.sex')
    dob = serializers.DateField(source='userprofile.dob')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'dob', 'about', 'sex')

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile', None)
        user = super(UserSerializer, self).create(validated_data)
        self.create_or_update_profile(user, profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', None)
        self.create_or_update_profile(instance, profile_data)
        return super(UserSerializer, self).update(instance, validated_data)

    def create_or_update_profile(self, user, profile_data):
        profile, created = UserProfile.objects.get_or_create(user=user, defaults=profile_data)
        if not created and profile_data is not None:
            super(UserSerializer, self).update(profile, profile_data)

