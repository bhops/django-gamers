from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.fields import empty
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserProfile
from users.serializers import UserProfileSerializer, UserSerializer
from utils.permissions import UserListAndCreatePermissions

class CurrentUserProfile(APIView):
    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

class UserList(generics.ListCreateAPIView):
    permission_classes = (UserListAndCreatePermissions,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (UserListAndCreatePermissions,)
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer

    def get_serializer(self, instance=None, data=empty, many=False, partial=False):
        if self.request.method == 'PUT':
            return UserSerializer(instance=instance, data=data, many=many, partial=True)
        else:
            return UserSerializer(instance=instance, data=data, many=many, partial=False)
