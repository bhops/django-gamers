from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from games.models import Game, Platform
from games.serializers import GameSerializer, PlatformSerializer

class GameViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

class PlatformViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()

    @list_route()
    def games(self, request, *args, **kwargs):
        platform = self.queryset[0]
        games = platform.games

        return Response(GameSerializer(games, many=True).data)
