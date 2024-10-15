from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class RoleModels(NamedDateTimeModel):

    def __str__(self):
        return self.name
