from django.contrib import admin

from employee.models.direction_models import DirectionModels
from employee.models.employe_models import EmployeModels
from employee.models.leave_models import LeaveModels

# Register your models here.
admin.site.register(LeaveModels)
admin.site.register(EmployeModels)
admin.site.register(DirectionModels)
