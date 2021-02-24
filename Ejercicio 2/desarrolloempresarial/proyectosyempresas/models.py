from django.db import models #El modulo models contiene la clase models.Model de la cual heredan los modelos
import uuid # Se usa para establecer id como llave primaria (primary_key)

# Create your models here.

class EtapaProyecto(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 30, null = True, blank = False, verbose_name = 'Etapa actual del proyecto*:') # Obligatorio

    class Meta:
        verbose_name_plural = 'Etapas de proyectos'

    def __str__(self):
        return '{0}'.format(self.nombre)

class ActividadEconomica(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 80, null = False, blank = False, verbose_name = 'Actividad economica*:') # Obligatorio

    class Meta:
        verbose_name_plural = 'Actividades economicas'

    def __str__(self):
        return '{0}'.format(self.id)      
        

class Persona(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 80, null = False, blank = False, verbose_name = 'Nombre de la persona*:') # Obligatorio
    id_persona = models.CharField(max_length = 80, null = False, blank = False, verbose_name = 'Identificación de la persona*:') # Obligatorio

    def __str__(self):
        return '{0}'.format(self.id_persona)

        


class ProyectoEmpresarial(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 60, null = False, blank = False, verbose_name = 'Nombre del proyecto*:') # Obligatorio
    descripcion = models.TextField(null = False, blank = False, verbose_name = 'Descripcion del proyecto*:')
    etapa_id = models.ForeignKey(EtapaProyecto, on_delete = models.SET_NULL, null = True, blank = True, help_text = 'Identifique la etapa en la cual se encuentra el proyecto')
    fecha_inicio = models.DateField(null = True, blank = True, verbose_name = 'Inicio del proyecto:', help_text = 'Escriba o seleccione la fecha de inicio del proyecto')
    actividad_economica = models.ForeignKey(ActividadEconomica, on_delete = models.SET_NULL, null = True, blank = True, help_text = 'Seleccione una actividad economica')
    cantidad_empleados = models.IntegerField(null = True, blank = True, verbose_name = 'Numero de empleados:')
    facturacion_mensual_aprox = models.IntegerField(null = True, blank = True, verbose_name = 'Facturacion mensual:', help_text = 'Valor aproximado de facturacion mensual')
    productos = models.TextField(null = True, blank = True)
    servicios = models.TextField(null = True, blank = True)
    tipo_mercado = models.CharField(max_length = 5, null = True, blank = True, verbose_name = 'Tipo de mercado:')
    numero_integrantes = models.CharField(max_length = 3, null = True, blank = True, verbose_name = 'Cantidad de integrantes:')
    persona_contacto = models.ForeignKey(Persona, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Persona contacto:')

    class Meta:
        verbose_name_plural = 'Proyectos empresariales'

    def __str__(self):
        return '{0}'.format(self.id)
        

class TamanoEmpresa(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 80, null = False, blank = False, verbose_name = 'Tipo*:', help_text = 'Ingrese una breve descripcion de acuerdo al tamaño, ej: PYME') # Obligatorio

    class Meta:
        verbose_name_plural = 'Tamaños de empresas'

    def __str__(self):
        return '{0}'.format(self.id)       
       

class TipoSociedad(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 80, null = False, blank = False, verbose_name = 'Tipo de sociedad*:', help_text = 'Escriba el tipo de sociedad para la empresa, ej: S.A.S') # Obligatorio

    class Meta:
        verbose_name_plural = 'Tipos de sociedades'

    def __str__(self):
        return '{0}'.format(self.id)
        


class Empresa(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nit = models.CharField(max_length = 11, null = False, blank = False, verbose_name = 'Nit*:') # Obligatorio
    razon_social = models.CharField(max_length = 30, null = False, blank = False, verbose_name = 'Razon Social*:') # Obligatorio
    fecha_formalizacion = models.CharField(max_length = 30, null = False, blank = False, verbose_name = 'Fecha de formalizacion*:', help_text = 'Fecha en que la empresa se constituyo legalmente') # Obligatorio
    tamano_empresa = models.ForeignKey(TamanoEmpresa, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Tamaño de la empresa:')
    tipo_sociedad_id = models.ForeignKey(TipoSociedad, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Sociedad:', help_text = 'Seleccione una identificacion para el tipo de sociedad')
    cubrimiento = models.CharField(max_length = 1, null = True, blank = True, verbose_name = 'Cubrimiento:' , help_text = 'Zona de cubrimiento de la empres')
    proyecto_empresarial_id = models.ForeignKey(ProyectoEmpresarial, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Proyecto empresarial:', help_text = 'Seleccione una identificacion para el proyecto empresarial')

    
class ModeloNegocio(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    proyecto_empresarial_id = models.ForeignKey(ProyectoEmpresarial, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Proyecto empresarial:')
    quien_ayudara = models.TextField(max_length = 1000, null = True, blank = True, verbose_name = '¿Quién ayudara?:')
    como_hace = models.TextField(max_length = 1000, null = True, blank = True, verbose_name = '¿Cómo hace?:')
    que_haces = models.TextField(max_length = 1000, null = True, blank = True, verbose_name = '¿Qué haces?:')
    como_interactuas = models.TextField(max_length = 1000, null = True, blank = True, verbose_name = '¿Cómo interactúas?:')
    a_quien_ayudas = models.TextField(max_length = 1000, null = True, blank = True, verbose_name = '¿A quién ayudas?:')
    que_necesitas = models.TextField(max_length = 1000, null = True, blank = True, verbose_name = '¿Qué necesitas?:')
    como_alcanzarlos = models.TextField(max_length = 1000, null = True, blank = True, verbose_name = '¿Cómo alcanzarlos?:')
    cual_sera_costo = models.TextField(max_length = 1000, null = True, blank = True, verbose_name = '¿Cuál sera el costo?:')
    cuanto_ganaras = models.TextField(max_length = 1000, null = True, blank = True, verbose_name = '¿Cuánto ganarás?:')
    

    class Meta:
        verbose_name_plural = 'Modelos de negocio'

    def __str__(self):
        return '{0}'.format(self.id)

class Profesion(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 80, null = False, blank = False, verbose_name = 'Profesion*:') # Obligatorio

    class Meta:
        verbose_name_plural = 'Profesiones'

    def __str__(self):
        return '{0}'.format(self.nombre)
    

class Ocupacion(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 80, null = False, blank = False, verbose_name = 'Ocupacion*:') # Obligatorio

    class Meta:
        verbose_name_plural = 'Ocupaciones'

    def __str__(self):
        return '{0}'.format(self.nombre)

class NivelEstudio(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 80, null = False, blank = False, verbose_name = 'Nivel de estudio*:') # Obligatorio

    class Meta:
        verbose_name_plural = 'Niveles de estudio'
        

    def __str__(self):
        return '{0}'.format(self.nombre)

class Integrante(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre_completo = models.CharField(max_length = 80, null = False, blank = False, verbose_name = 'Nombre completo*:') # Obligatorio
    cargo = models.CharField(max_length = 30, null = True, blank = True, verbose_name = 'Cargo:')
    profesion = models.ForeignKey(Profesion, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Profesión:')
    ocupacion = models.ForeignKey(Ocupacion, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Ocupación:')
    nivel_estudio_id = models.ForeignKey(NivelEstudio, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Nivel de estudio:', help_text = 'Seleccione una identificacion para el nivel de estudios')
    edad = models.IntegerField(null = True, blank = True, verbose_name = 'Edad:')
    sexo = models.CharField(max_length = 2, null = True, blank = True, verbose_name = 'Sexo:')
    #------------------------------------------------
    BOOL_CHOICES = ((True, 'Si'), (False, 'No'))
    es_lider = models.BooleanField(null = True, blank = True, choices = BOOL_CHOICES, verbose_name = '¿Es lider?:')

    proyecto_empresarial = models.ForeignKey(ProyectoEmpresarial, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Proyecto empresarial:')

    
class Pais(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 50, null = False, blank = False, verbose_name = 'Nombre del Pais*:') # Obligatorio

    class Meta:
        verbose_name_plural = 'Paises'

    def __str__(self):
        return '{0}'.format(self.nombre)

class Departamento(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 50, null = False, blank = False, verbose_name = 'Nombre del departamento*:') # Obligatorio

    def __str__(self):
        return '{0}'.format(self.nombre)

class Municipio(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 50, null = False, blank = False, verbose_name = 'Nombre del municipio*:') # Obligatorio

    def __str__(self):
        return '{0}'.format(self.nombre)

class DivisionTerritorial(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 50, null = False, blank = False, verbose_name = 'Division territorial*:') # Obligatorio

    class Meta:
        verbose_name_plural = 'Divisiones territoriales'

    def __str__(self):
        return '{0}'.format(self.nombre)

class Barrio(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 30, null = False, blank = False, verbose_name = 'Nombre del barrio*:') # Obligatorio

    def __str__(self):
        return '{0}'.format(self.nombre)



class InformacionContactoEmpresa(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    celular = models.CharField(max_length = 15, null = False, blank = False, verbose_name = 'Celular 1*:') # Obligatorio
    celular_2 = models.CharField(max_length = 15, null = True, blank = True, verbose_name = 'Celular 2:')
    telefono = models.CharField(max_length = 15, null = True, blank = True, verbose_name = 'Telefono fijo:')
    correo_electronico = models.EmailField(max_length = 60, null = True, blank = True, verbose_name = 'Email:' )
    instagram = models.CharField(max_length = 60, null = True, blank = True, verbose_name = 'Insatagram:')
    facebook = models.CharField(max_length = 60, null = True, blank = True, verbose_name = 'Facebook:')
    pais_id = models.ForeignKey(Pais, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Pais:', help_text = 'Seleccione una identificación para el pais')
    departamento_id = models.ForeignKey(Departamento, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Departamento:', help_text = 'Seleccione una identificación para el departamento')
    municipio_id = models.ForeignKey(Municipio, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Municipio:', help_text = 'Seleccione una identificación para el municipio')
    division_territorial_id = models.ForeignKey(DivisionTerritorial, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Division territorial:', help_text = 'Seleccione una identificación para la division territorial')
    barrio_id = models.ForeignKey(Barrio, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Barrio:', help_text = 'Seleccione una identificación para el barrio')
    otro_barrio = models.CharField(max_length = 40, null = True, blank = True, verbose_name = 'Barrio 2:')
    direccion = models.CharField(max_length = 40, null = True, blank = True, verbose_name = 'Dirección:')
    proyecto_empresarial_id = models.ForeignKey(ProyectoEmpresarial, on_delete = models.SET_NULL, null = True, blank = True, verbose_name = 'Id. Proyecto empresarial:', help_text = 'Seleccione una identificacion de proyecto empresarial')

    class Meta:
        verbose_name_plural = 'Contactos de empresas'

    
        




