from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all() #filter(user_displayName='条件')
    serializer_class = UserSerializer