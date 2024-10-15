from rest_framework import viewsets
from users.models.role_models import RoleModels
from users.serializers.role_serializer import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = RoleModels.objects.all()