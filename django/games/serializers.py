from rest_framework import serializers
from games.models import Game, Platform

class PlatformSerializer(serializers.ModelSerializer):
#    games = GameSerializer(many=True)
    class Meta:
        model = Platform


class GameSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()
    class Meta:
        model = Game
        exclude = ('gr_url',)
