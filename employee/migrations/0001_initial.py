# Generated by Django 5.0 on 2024-10-13 04:22

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('sexe', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=50)),
                ('contrat', models.CharField(choices=[('CDI', 'CDI'), ('CDD', 'CDD'), ('STAGE', 'STAGE'), ('TEMPLATE_PARTIEL', 'TEMPLATE_PARTIEL')], max_length=50)),
                ('matricule', models.CharField(max_length=6)),
                ('salaire', models.CharField(max_length=60)),
                ('date_embauche', models.DateField(default=datetime.datetime(2024, 1, 1, 0, 0))),
                ('department', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('social_secure_number', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DirectionModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=180)),
                ('description', models.TextField()),
                ('employe_chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='employee.employemodels')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeaveModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=180)),
                ('type_de_conge', models.CharField(choices=[('vacation', 'Vacation'), ('sick', 'Sick Leave')], max_length=50)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('statut_manager', models.BooleanField(default=False)),
                ('statut_rh', models.BooleanField(default=False)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holidays', to='employee.employemodels')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
