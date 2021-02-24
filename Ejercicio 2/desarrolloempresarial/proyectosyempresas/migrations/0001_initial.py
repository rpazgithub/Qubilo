# Generated by Django 3.1.6 on 2021-02-21 04:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadEconomica',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, verbose_name='Actividad economica:')),
            ],
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del barrio:')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del departamento:')),
            ],
        ),
        migrations.CreateModel(
            name='DivisionTerritorial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Division territorial:')),
            ],
        ),
        migrations.CreateModel(
            name='EtapaProyecto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del proyecto:')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del municipio:')),
            ],
        ),
        migrations.CreateModel(
            name='NivelEstudio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, verbose_name='Nivel de estudio:')),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, verbose_name='Ocupacion:')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Pais:')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre de la persona:')),
                ('id_persona', models.CharField(max_length=80, verbose_name='Identificación de la persona:')),
            ],
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, verbose_name='Profesion:')),
            ],
        ),
        migrations.CreateModel(
            name='TamanoEmpresa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(help_text='Ingrese una breve descripcion de acuerdo al tamaño, ej: PYME', max_length=80, verbose_name='Tipo:')),
            ],
        ),
        migrations.CreateModel(
            name='TipoSociedad',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(help_text='Escriba el tipo de sociedad para la empresa, ej: S.A.S', max_length=80, verbose_name='Tipo de sociedad:')),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoEmpresarial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre del proyecto:')),
                ('descripcion', models.TextField(verbose_name='Descripcion del proyecto:')),
                ('fecha_inicio', models.DateField(blank=True, help_text='Escriba o seleccione la fecha de inicio del proyecto', null=True, verbose_name='Inicio del proyecto:')),
                ('cantidad_empleados', models.IntegerField(blank=True, null=True, verbose_name='Numero de empleados:')),
                ('facturacion_mensual_aprox', models.IntegerField(blank=True, help_text='Valor aproximado de facturacion mensual', null=True, verbose_name='Facturacion mensual:')),
                ('productos', models.TextField(blank=True, null=True)),
                ('servicios', models.TextField(blank=True, null=True)),
                ('tipo_mercado', models.CharField(blank=True, max_length=5, null=True, verbose_name='Tipo de mercado:')),
                ('numero_integrantes', models.CharField(blank=True, max_length=3, null=True, verbose_name='Cantidad de integrantes:')),
                ('actividad_economica', models.ForeignKey(blank=True, help_text='Seleccione una actividad economica', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.actividadeconomica')),
                ('etapa_id', models.ForeignKey(blank=True, help_text='Identifique la etapa en la cual se encuentra el proyecto', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.etapaproyecto')),
                ('persona_contacto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.persona', verbose_name='Persona contacto:')),
            ],
        ),
        migrations.CreateModel(
            name='ModeloNegocio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quien_ayudara', models.TextField(blank=True, max_length=1000, null=True, verbose_name='¿Quién ayudara?:')),
                ('como_hace', models.TextField(blank=True, max_length=1000, null=True, verbose_name='¿Cómo hace?:')),
                ('que_haces', models.TextField(blank=True, max_length=1000, null=True, verbose_name='¿Qué haces?:')),
                ('como_interactuas', models.TextField(blank=True, max_length=1000, null=True, verbose_name='¿Cómo interactúas?:')),
                ('a_quien_ayudas', models.TextField(blank=True, max_length=1000, null=True, verbose_name='¿A quién ayudas?:')),
                ('que_necesitas', models.TextField(blank=True, max_length=1000, null=True, verbose_name='¿Qué necesitas?:')),
                ('como_alcanzarlos', models.TextField(blank=True, max_length=1000, null=True, verbose_name='¿Cómo alcanzarlos?:')),
                ('cual_sera_costo', models.TextField(blank=True, max_length=1000, null=True, verbose_name='¿Cuál sera el costo?:')),
                ('cuanto_ganaras', models.TextField(blank=True, max_length=1000, null=True, verbose_name='¿Cuánto ganarás?:')),
                ('proyecto_empresarial_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.proyectoempresarial', verbose_name='Id. Proyecto empresarial:')),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=80, verbose_name='Nombre completo:')),
                ('cargo', models.CharField(blank=True, max_length=30, null=True, verbose_name='Cargo:')),
                ('edad', models.IntegerField(blank=True, null=True, verbose_name='Edad:')),
                ('sexo', models.CharField(blank=True, max_length=2, null=True, verbose_name='Sexo:')),
                ('es_lider', models.BooleanField(blank=True, null=True, verbose_name='¿Es lider?:')),
                ('nivel_estudio_id', models.ForeignKey(blank=True, help_text='Seleccione una identificacion para el nivel de estudios', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.nivelestudio', verbose_name='Id. Nivel de estudio:')),
                ('ocupacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.ocupacion', verbose_name='Ocupación:')),
                ('profesion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.profesion', verbose_name='Profesión:')),
                ('proyecto_empresarial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.proyectoempresarial', verbose_name='Proyecto empresarial:')),
            ],
        ),
        migrations.CreateModel(
            name='InformacionContactoEmpresa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('celular', models.CharField(max_length=15, verbose_name='Celular 1:')),
                ('celular_2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Celular 2:')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono fijo:')),
                ('correo_electronico', models.EmailField(blank=True, max_length=60, null=True, verbose_name='Email:')),
                ('instagram', models.CharField(blank=True, max_length=60, null=True, verbose_name='Insatagram:')),
                ('facebook', models.CharField(blank=True, max_length=60, null=True, verbose_name='Facebook:')),
                ('otro_barrio', models.CharField(blank=True, max_length=40, null=True, verbose_name='Barrio 2:')),
                ('direccion', models.CharField(blank=True, max_length=40, null=True, verbose_name='Dirección:')),
                ('barrio_id', models.ForeignKey(blank=True, help_text='Seleccione una identificación para el barrio', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.barrio', verbose_name='Id. Barrio:')),
                ('departamento_id', models.ForeignKey(blank=True, help_text='Seleccione una identificación para el departamento', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.departamento', verbose_name='Id. Departamento:')),
                ('division_territorial_id', models.ForeignKey(blank=True, help_text='Seleccione una identificación para la division territorial', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.divisionterritorial', verbose_name='Id. Division territorial:')),
                ('municipio_id', models.ForeignKey(blank=True, help_text='Seleccione una identificación para el municipio', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.municipio', verbose_name='Id. Municipio:')),
                ('pais_id', models.ForeignKey(blank=True, help_text='Seleccione una identificación para el pais', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.pais', verbose_name='Id. Pais:')),
                ('proyecto_empresarial_id', models.ForeignKey(blank=True, help_text='Seleccione una identificacion de proyecto empresarial', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.proyectoempresarial', verbose_name='Id. Proyecto empresarial:')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nit', models.CharField(max_length=11, verbose_name='Nit:')),
                ('razon_social', models.CharField(max_length=30, verbose_name='Razon Social:')),
                ('fecha_formalizacion', models.CharField(help_text='Fecha en que la empresa se constituyo legalmente', max_length=30, verbose_name='Fecha de formalizacion:')),
                ('cubrimiento', models.CharField(blank=True, help_text='Zona de cubrimiento de la empres', max_length=1, null=True, verbose_name='Cubrimiento:')),
                ('proyecto_empresarial_id', models.ForeignKey(blank=True, help_text='Seleccione una identificacion para el proyecto empresarial', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.proyectoempresarial', verbose_name='Id. Proyecto empresarial:')),
                ('tamano_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.tamanoempresa', verbose_name='Tamaño de la empresa:')),
                ('tipo_sociedad_id', models.ForeignKey(blank=True, help_text='Seleccione una identificacion para el tipo de sociedad', null=True, on_delete=django.db.models.deletion.SET_NULL, to='proyectosyempresas.tiposociedad', verbose_name='Id. Sociedad:')),
            ],
        ),
    ]
