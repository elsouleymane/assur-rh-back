from rest_framework import viewsets

from employee.models.leave_models import LeaveModels
from employee.serializers.leave_serializer import LeaveSerializer


class LeaveViewSet(viewsets.ModelViewSet):
    serializer_class = LeaveSerializer
    queryset = LeaveModels.objects.all()
