from rest_framework import serializers
from games.models import Game, Platform

class GameSerializer(serializers.ModelSerializer):
    platform = serializers.SlugRelatedField(queryset=Platform.objects.all(), slug_field='slug')
    slug = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = Game

class PlatformSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = Platform
