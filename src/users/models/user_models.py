from django.db import models
from users.models.role_models import RoleModels
from django.contrib.auth.models import AbstractUser
from base.models.helpers.date_time_model import DateTimeModel


class UserModels(DateTimeModel, AbstractUser):
    role = models.ForeignKey(RoleModels, on_delete=models.CASCADE, null=True, related_name='users')
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    profil_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.username
