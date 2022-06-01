# Generated by Django 4.0.4 on 2022-05-27 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('ramal', models.CharField(blank=True, max_length=255, verbose_name='Ramal')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name='Email')),
                ('data_aniversario', models.DateTimeField(blank=True, max_length=255, verbose_name='Data Aniversário')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Criação')),
                ('status', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('cargo', models.ForeignKey(on_delete=models.SET('Vazio'), to='colaboradores.cargo', verbose_name='Cargo')),
                ('setor', models.ForeignKey(on_delete=models.SET('Vazio'), to='colaboradores.setor', verbose_name='Setor')),
            ],
        ),
    ]