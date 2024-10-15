from rest_framework import viewsets
from users.models.user_models import UserModels
from users.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModels.objects.all()