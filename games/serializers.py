from rest_framework import serializers
from games.models import Game, Platform

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
