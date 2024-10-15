from rest_framework import viewsets

from users.models.menu_models import MenuModels
from users.serializers.menu_serializer import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = MenuModels.objects.all()
