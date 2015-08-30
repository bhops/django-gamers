from .models import LookingForPost, Schedule
from .serializers import LookingForPostSerializer, ScheduleSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

class LookingForPostList(generics.ListAPIView):
    queryset = LookingForPost.objects.all()
    serializer_class = LookingForPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

class LookingForPostListGame(generics.ListAPIView):
    serializer_class = LookingForPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def get_queryset(self):
        game = self.kwargs['game']
        return LookingForPost.objects.filter(game__slug=game)

class LookingForPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LookingForPost.objects.all()
    serializer_class = LookingForPostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class ScheduleDetail(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer

    def retrieve(self, request, username):
        queryset = Schedule.objects.filter(user__username=username)
        serializer = ScheduleSerializer(queryset, many=True)
        return Response(serializer.data)
