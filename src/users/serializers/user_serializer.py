from rest_framework import serializers
from users.models.user_models import UserModels


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModels
        fields = "__all__"
