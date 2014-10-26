#coding:utf-8
from django.contrib import admin
from models import Postulante, Instalacion, Contratado
# Register your models here.
class PostulanteAdmin(admin.ModelAdmin):
    list_display= ( 'nombre_completo',  'comuna',
          'fecha',   'ha_sido_condenado_o_detenido', 'industrial','contratado',  'observaciones', 'medio',  )
    list_filter =  (  'contratado', 'industrial', 'ha_sido_condenado_o_detenido',   'fecha', 'comuna',  'creado_por',)
#    list_editable = ('ha_sido_condenado_o_detenido',)
    search_fields = ('nombres', 'apellidos', 'rut', 'observaciones') 
    fieldsets = (
        ('', {'fields': ('fecha', 'medio')}),
        ('Información personal', {'fields': ('nombres','apellidos', 'rut','fecha_de_nacimiento', 'nacionalidad',
        'sexo', 'escolaridad', )}),
        ('Información de contacto', {'fields': ('domicilio', 'comuna', 'email', 'telefono',
        'telefono_emergencia')}),
        ('Otros', {'fields': (  ('ha_sido_condenado_o_detenido', 'motivo'), 'industrial' ,
         ('contratado', 'fecha_contratacion'), 'instalacion', ('os10', 'vencimiento'), 'observaciones' , )}),
         #('fecha_contratacion', 'instalacion')#
    )


class ContratadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'fecha_contratacion', 'instalacion', 'fecha_de_nacimiento', 'os10', 'vencimiento', )
    fieldsets = (
    ('', {'fields':('nombres', 'apellidos', 'fecha_de_nacimiento', ('os10', 'vencimiento'), 'instalacion')}),
     
    )
    list_filter = ('os10', 'fecha_contratacion')

admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Instalacion)
admin.site.register(Contratado, ContratadoAdmin)
