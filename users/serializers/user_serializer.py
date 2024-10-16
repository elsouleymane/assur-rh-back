from rest_framework import serializers
from users.models.user_models import UserModels


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModels
        fields = "__all__"

class ChangePasswordSerializer(serializers.Serializer):
    model = UserModels

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)