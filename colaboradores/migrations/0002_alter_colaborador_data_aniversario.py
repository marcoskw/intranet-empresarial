# Generated by Django 4.0.4 on 2022-05-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='data_aniversario',
            field=models.CharField(blank=True, max_length=10, verbose_name='Aniversário'),
        ),
    ]
