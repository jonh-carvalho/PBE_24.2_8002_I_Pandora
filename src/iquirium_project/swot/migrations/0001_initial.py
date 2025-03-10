# Generated by Django 5.1.2 on 2024-11-01 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forca', models.CharField(max_length=100)),
                ('fraqueza', models.CharField(max_length=100)),
                ('oportunidade', models.CharField(max_length=100)),
                ('ameaca', models.CharField(max_length=100)),
                ('analiseSwot', models.CharField(max_length=100)),
                ('dataUltimaAnalise', models.DateTimeField(auto_now_add=True)),
                ('periodoEntreAnalises', models.IntegerField()),
                ('statusConclusao', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swot', to='perfil.perfil')),
            ],
        ),
    ]
