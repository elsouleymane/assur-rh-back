from django.contrib import admin

from documents.models.document_models import DocumentModels
from users.models.menu_models import MenuModels
from users.models.permissions_models import PermissionModels
from users.models.role_models import RoleModels
from users.models.user_models import UserModels

# Register your models here.
admin.site.register(UserModels)
admin.site.register(PermissionModels)
admin.site.register(RoleModels)
admin.site.register(MenuModels)
admin.site.register(DocumentModels)
