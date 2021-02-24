# Generated by Django 3.1.6 on 2021-02-21 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectosyempresas', '0002_auto_20210221_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividadeconomica',
            options={'verbose_name': 'Actividades economica'},
        ),
        migrations.AlterModelOptions(
            name='divisionterritorial',
            options={'verbose_name': 'Divisiones territoriale'},
        ),
        migrations.AlterModelOptions(
            name='etapaproyecto',
            options={'verbose_name': 'Etapas de proyecto'},
        ),
        migrations.AlterModelOptions(
            name='informacioncontactoempresa',
            options={'verbose_name': 'Contactos de empresa'},
        ),
        migrations.AlterModelOptions(
            name='modelonegocio',
            options={'verbose_name': 'Modelos de negocio'},
        ),
        migrations.AlterModelOptions(
            name='nivelestudio',
            options={'verbose_name': 'Nivel de estudio'},
        ),
        migrations.AlterModelOptions(
            name='ocupacion',
            options={'verbose_name': 'Ocupacione'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'Pai'},
        ),
        migrations.AlterModelOptions(
            name='profesion',
            options={'verbose_name': 'Profesione'},
        ),
        migrations.AlterModelOptions(
            name='proyectoempresarial',
            options={'verbose_name': 'Proyectos empresariale'},
        ),
        migrations.AlterModelOptions(
            name='tamanoempresa',
            options={'verbose_name': 'Tamaños de empresa'},
        ),
        migrations.AlterModelOptions(
            name='tiposociedad',
            options={'verbose_name': 'Tipos de sociedade'},
        ),
    ]