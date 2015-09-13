from rest_framework import generics, mixins
from games.models import Game, Platform
from games.serializers import GameSerializer, PlatformSerializer

class GameList(mixins.ListModelMixin,
               generics.GenericAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)

class GameDetail(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    lookup_field = 'slug'
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PlatformList(mixins.ListModelMixin,
                   generics.GenericAPIView):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PlatformDetail(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    lookup_field = 'slug'
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
