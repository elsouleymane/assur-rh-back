from rest_framework import serializers
from employee.models.leave_models import LeaveModels


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveModels
        fields = "__all__"