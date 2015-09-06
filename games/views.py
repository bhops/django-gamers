from rest_framework import generics
from games.models import Game, Platform
from games.serializers import GameSerializer, PlatformSerializer
from utils.permissions import IsAdminOrReadOnly

class GameList(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlatformList(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
