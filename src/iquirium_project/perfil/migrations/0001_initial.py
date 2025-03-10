# Generated by Django 5.1.2 on 2024-11-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro')], max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('experiencia', models.CharField(max_length=100)),
                ('carreira_atual', models.CharField(max_length=100)),
                ('nivel_carreira_atual', models.IntegerField()),
            ],
        ),
    ]
