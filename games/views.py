from rest_framework import generics
from users.permissions import IsEditorPermission
from .models import Game, Developer
from .serializers import GameSerializer, DeveloperSerializer


class GameCreateView(generics.CreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsEditorPermission]


class DeveloperCreateView(generics.CreateAPIView):
    serializer_class = DeveloperSerializer
    permission_classes = [IsEditorPermission]
