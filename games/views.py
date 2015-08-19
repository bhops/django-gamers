from games.models import Game, OwnedGame, Platform
from games.serializers import GameSerializer, OwnedGameSerializer, PlatformSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'games': reverse('game-list', request=request, format=format),
        'platforms': reverse('platform-list', request=request, format=format)
    })

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlatformList(generics.ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class OwnedGameList(generics.ListCreateAPIView):
    serializer_class = OwnedGameSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return OwnedGame.objects.filter(user__username=username)

