from django.db import models
from employee.models.employe_models import EmployeModels
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class LeaveModels(NamedDateTimeModel):
    TYPE_CONGE = [
        ('vacation', 'Vacation'),
        ('sick', 'Sick Leave'),
    ]

    type_de_conge = models.CharField(max_length=50, choices=TYPE_CONGE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    commentaire = models.TextField(blank=True, null=True)
    employe = models.ForeignKey(EmployeModels, on_delete=models.CASCADE, related_name='holidays')
    statut_manager = models.BooleanField(default=False)
    statut_rh = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type_de_conge} - {self.employe.first_name}"