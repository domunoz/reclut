#coding:utf-8
from django.contrib import admin
from models import Postulante, Instalacion
# Register your models here.
class PostulanteAdmin(admin.ModelAdmin):
    list_display= ( 'nombre_completo',  'comuna',
        'telefono',  'fecha', 'contratado', 'observaciones', 'creado_por'  )
    list_filter =  (  'contratado', 'creado_por', 'fecha', 'sexo'  ,'comuna',  )
#    list_editable = ('comuna',)
    search_fields = ('nombres', 'apellidos', 'rut', 'observaciones') 
    fieldsets = (
        ('', {'fields': ('fecha', 'medio')}),
        ('Información personal', {'fields': ('nombres','apellidos', 'rut','fecha_de_nacimiento', 'nacionalidad',
        'sexo', 'escolaridad', ('estado_civil', 'hijos'), 'jubilado', 'afp', 'sistema_de_salud')}),
        ('Información de contacto', {'fields': ('domicilio', 'comuna', 'email', 'telefono',
        'telefono_emergencia')}),
        ('Otros', {'fields': ( 'cargo',('os10', 'vencimiento'), ('ha_sido_condenado_o_detenido', 'motivo'), ('industrial', 'retail'),
         ('visto_bueno', 'contratado'), ('fecha_contratacion', 'instalacion'), 'observaciones' , )}),
    )


admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Instalacion)
