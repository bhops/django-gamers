from rest_framework import serializers
from .models import LookingForPost, Schedule, ScheduleBlock
from games.serializers import GameSerializer

class LookingForPostSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = LookingForPost

class ScheduleBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleBlock
        fields = ('day_of_week', 'time_to', 'time_from',)

class ScheduleSerializer(serializers.ModelSerializer):
    blocks = ScheduleBlockSerializer(many=True)
    class Meta:
        model = Schedule
        fields = ('blocks',)
