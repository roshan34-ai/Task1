from urllib import response
from requests import Response, patch
from rest_framework import generics
from taskapp.permissions import IsTeamLeader
from .permissions import IsTeamLeader, IsTeamMembar
from .models import CustomUser, Task, Team
from rest_framework.permissions import AllowAny , IsAuthenticated
from .serializers import CustomUserSerializer, TaskSerializer, TeamSerializer
from rest_framework.decorators import api_view, permission_classes


from taskapp import serializers

class TeamAPIView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (AllowAny,)
    
class UserRegister(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


class UpdateTaskView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsTeamLeader,)

class UpdateStatusView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,IsTeamMembar)
