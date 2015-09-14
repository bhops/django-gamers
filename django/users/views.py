from django.contrib.auth.models import User
from rest_framework import mixins, serializers, status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.settings import api_settings
from users.serializers import UserSerializer, UserCreateSerializer, UserProfileSerializer
from users.models import UserProfile
from utils.permissions import UserListAndCreatePermissions

class Users(mixins.ListModelMixin,
            viewsets.GenericViewSet):
    lookup_field = 'username'
    permission_classes = (UserListAndCreatePermissions,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @detail_route()
    def validation(self, request, *args, **kwargs):
        raise serializers.ValidationError('Uh oh')


    @detail_route()
    def profile(self, request, *args, **kwargs):
        self.resource_name = False

        user = self.queryset[0]
        profile = user.profile

        data = {
            'user': UserSerializer(user, many=False).data,
            'profile': UserProfileSerializer(profile, many=False).data
        }
        return Response(data)
