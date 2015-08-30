from rest_framework import serializers
from games.models import Game, OwnedGame, Platform

class GameSerializer(serializers.ModelSerializer):
    platform = serializers.SlugRelatedField(queryset=Platform.objects.all(), slug_field='name')
    slug = serializers.SlugField(required=False, allow_null=True)
    class Meta:
        model = Game

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform

class OwnedGameSerializer(serializers.ModelSerializer):
    game = GameSerializer(many=False, read_only=True)
    class Meta:
        model = OwnedGame
        fields = ('game',)
