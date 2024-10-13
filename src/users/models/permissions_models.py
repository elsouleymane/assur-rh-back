from django.db import models
from users.models.role_models import RoleModels
from users.models.menu_models import MenuModels


class PermissionModels(models.Model):
    role = models.ForeignKey(RoleModels, on_delete=models.CASCADE, related_name='permissions')
    menu = models.ForeignKey(MenuModels, on_delete=models.CASCADE, related_name='permissions')

    def __str__(self):
        return f"{self.role} - {self.menu}"