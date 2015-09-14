from django.contrib.auth.models import User
from rest_framework import mixins, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from users.serializers import UserSerializer, UserProfileSerializer
from users.models import UserProfile
from utils.permissions import UserListAndCreatePermissions

class Users(mixins.ListModelMixin,
            mixins.CreateModelMixin,
            viewsets.GenericViewSet):
    lookup_field = 'username'
    permission_classes = (UserListAndCreatePermissions,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
