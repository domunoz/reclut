#coding:utf-8
from django.contrib import admin
from models import Postulante, Instalacion
# Register your models here.
class PostulanteAdmin(admin.ModelAdmin):
    list_display= ( 'nombre_completo',  'comuna',
          'fecha', 'medio',   'ha_sido_condenado_o_detenido', 'industrial','contratado', 'creado_por'  )
    list_filter =  (  'contratado', 'industrial', 'ha_sido_condenado_o_detenido',   'fecha', 'comuna',  'creado_por',)
#    list_editable = ('ha_sido_condenado_o_detenido',)
    search_fields = ('nombres', 'apellidos', 'rut', 'observaciones') 
    fieldsets = (
        ('', {'fields': ('fecha', 'medio')}),
        ('Información personal', {'fields': ('nombres','apellidos', 'rut','fecha_de_nacimiento', 'nacionalidad',
        'sexo', 'escolaridad', ('estado_civil', 'hijos'), 'jubilado', 'afp', 'sistema_de_salud')}),
        ('Información de contacto', {'fields': ('domicilio', 'comuna', 'email', 'telefono',
        'telefono_emergencia')}),
        ('Otros', {'fields': (  ('ha_sido_condenado_o_detenido', 'motivo'), 'industrial' ,
         'contratado', ('os10', 'vencimiento'), 'observaciones' , )}),
         #('fecha_contratacion', 'instalacion')#
    )


admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Instalacion)
