from rest_framework import serializers
from employee.models.direction_models import DirectionModels


class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DirectionModels
        fields = "__all__"