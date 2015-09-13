from django.contrib.auth.models import User
from rest_framework import viewsets
from users.serializers import UserSerializer
from utils.permissions import UserListAndCreatePermissions

class Users(viewsets.ModelViewSet):
    lookup_field = 'username'
    permission_classes = (UserListAndCreatePermissions,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
