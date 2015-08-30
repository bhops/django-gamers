from users.models import UserProfile
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer
