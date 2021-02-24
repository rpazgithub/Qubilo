# Generated by Django 3.1.6 on 2021-02-21 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectosyempresas', '0007_auto_20210221_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadeconomica',
            name='nombre',
            field=models.CharField(max_length=80, verbose_name='Actividad economica*:'),
        ),
        migrations.AlterField(
            model_name='barrio',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre del barrio*:'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre del departamento*:'),
        ),
        migrations.AlterField(
            model_name='divisionterritorial',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Division territorial*:'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='fecha_formalizacion',
            field=models.CharField(help_text='Fecha en que la empresa se constituyo legalmente', max_length=30, verbose_name='Fecha de formalizacion*:'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nit',
            field=models.CharField(max_length=11, verbose_name='Nit*:'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='razon_social',
            field=models.CharField(max_length=30, verbose_name='Razon Social*:'),
        ),
        migrations.AlterField(
            model_name='etapaproyecto',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Etapa actual del proyecto*:'),
        ),
        migrations.AlterField(
            model_name='informacioncontactoempresa',
            name='celular',
            field=models.CharField(max_length=15, verbose_name='Celular 1*:'),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='es_lider',
            field=models.BooleanField(blank=True, choices=[(True, 'Si'), (False, 'No')], null=True, verbose_name='¿Es lider?:'),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='nombre_completo',
            field=models.CharField(max_length=80, verbose_name='Nombre completo*:'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre del municipio*:'),
        ),
        migrations.AlterField(
            model_name='nivelestudio',
            name='nombre',
            field=models.CharField(max_length=80, verbose_name='Nivel de estudio*:'),
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='nombre',
            field=models.CharField(max_length=80, verbose_name='Ocupacion*:'),
        ),
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre del Pais*:'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='id_persona',
            field=models.CharField(max_length=80, verbose_name='Identificación de la persona*:'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=80, verbose_name='Nombre de la persona*:'),
        ),
        migrations.AlterField(
            model_name='profesion',
            name='nombre',
            field=models.CharField(max_length=80, verbose_name='Profesion*:'),
        ),
        migrations.AlterField(
            model_name='proyectoempresarial',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion del proyecto*:'),
        ),
        migrations.AlterField(
            model_name='proyectoempresarial',
            name='nombre',
            field=models.CharField(max_length=60, verbose_name='Nombre del proyecto*:'),
        ),
        migrations.AlterField(
            model_name='tamanoempresa',
            name='nombre',
            field=models.CharField(help_text='Ingrese una breve descripcion de acuerdo al tamaño, ej: PYME', max_length=80, verbose_name='Tipo*:'),
        ),
        migrations.AlterField(
            model_name='tiposociedad',
            name='nombre',
            field=models.CharField(help_text='Escriba el tipo de sociedad para la empresa, ej: S.A.S', max_length=80, verbose_name='Tipo de sociedad*:'),
        ),
    ]
