from rest_framework import serializers
from employee.models.employe_models import EmployeModels


class EmployeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeModels
        fields = "__all__"