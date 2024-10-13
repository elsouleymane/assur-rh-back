from rest_framework import serializers
from users.models.menu_models import MenuModels


class MenuSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MenuModels
        fields = "__all__"