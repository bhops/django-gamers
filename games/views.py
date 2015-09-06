from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from games.models import Game, Platform
from games.serializers import GameSerializer, PlatformSerializer
from utils.permissions import IsAdminOrReadOnly

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'games': reverse('game-list', request=request, format=format),
        'platforms': reverse('platform-list', request=request, format=format)
    })

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
