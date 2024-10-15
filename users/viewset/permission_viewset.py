from rest_framework import viewsets

from users.models.permissions_models import PermissionModels
from users.serializers.permission_serializer import PermissionSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = PermissionModels.objects.all()