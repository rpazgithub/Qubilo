# Generated by Django 3.1.6 on 2021-02-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectosyempresas', '0006_auto_20210221_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapaproyecto',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Etapa actual del proyecto:'),
        ),
    ]