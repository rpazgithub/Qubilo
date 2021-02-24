from django.contrib import admin
from .models import EtapaProyecto, ActividadEconomica, TamanoEmpresa, TipoSociedad, ModeloNegocio, Profesion, Ocupacion, NivelEstudio, Pais, Departamento, Municipio, DivisionTerritorial, Barrio, Empresa, Persona,ProyectoEmpresarial, Integrante, InformacionContactoEmpresa

# Register your models here.

admin.site.register(EtapaProyecto)
admin.site.register(TipoSociedad)
admin.site.register(ModeloNegocio)
admin.site.register(Profesion)
admin.site.register(Ocupacion)
admin.site.register(NivelEstudio)
admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(DivisionTerritorial)
admin.site.register(Barrio)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nit', 'razon_social')

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id_persona', 'nombre')

class ProyectoEmpresarialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'persona_contacto')

class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cargo', 'profesion')

class InformacionContactoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('celular', 'correo_electronico')

class ActividadEconomicaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class TamanoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(ProyectoEmpresarial, ProyectoEmpresarialAdmin)
admin.site.register(Integrante, IntegranteAdmin)
admin.site.register(InformacionContactoEmpresa, InformacionContactoEmpresaAdmin)
admin.site.register(ActividadEconomica, ActividadEconomicaAdmin)
admin.site.register(TamanoEmpresa, TamanoEmpresaAdmin)


    
