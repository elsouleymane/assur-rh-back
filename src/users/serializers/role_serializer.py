from rest_framework import serializers
from users.models.role_models import RoleModels


class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RoleModels
        fields = "__all__"