# Generated by Django 3.1.6 on 2021-02-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectosyempresas', '0008_auto_20210221_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapaproyecto',
            name='nombre',
            field=models.CharField(max_length=30, null=True, verbose_name='Etapa actual del proyecto*:'),
        ),
    ]
