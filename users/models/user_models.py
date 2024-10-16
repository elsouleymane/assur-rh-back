from django.db import models
from users.models.role_models import RoleModels
from django.contrib.auth.models import AbstractUser, Group, Permission
from base.models.helpers.date_time_model import DateTimeModel


class UserModels(AbstractUser, DateTimeModel):
    role = models.ForeignKey(RoleModels, on_delete=models.CASCADE, null=True, related_name='users')
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    profil_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role', 'username']

    def __str__(self):
        return self.username
