from rest_framework import serializers
from users.models.permissions_models import PermissionModels


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PermissionModels
        fields = "__all__"