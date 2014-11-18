#coding:utf-8
from django.contrib import admin
from daterange_filter.filter import DateRangeFilter
from models import Postulante, Instalacion, Contratado, Supervisor, Cliente, Comuna, Region, Medio
# Register your models here.
class PostulanteAdmin(admin.ModelAdmin):
    list_display= ( 'fecha', 'medio1', 'nombres', 'apellidos',  'comuna', 'ha_sido_condenado_o_detenido', 'industrial', 
             'contratado', )#  'observaciones',  )
    list_filter =  (  'contratado',  ('fecha', DateRangeFilter),  'medio', 'comuna')
#    list_editable = ('ha_sido_condenado_o_detenido',)
    list_editable = ('medio', 'medio1',)

#    radio_fields = {'sexo': admin.VERTICAL, 'escolaridad': admin.HORIZONTAL }

    search_fields = ('nombres', 'apellidos', 'rut',) 
    fieldsets = (
        ('', {'fields': ('fecha', 'medio1', 'nombres','apellidos', 'rut', 'domicilio', 'comuna',
         'ubicacion',  'telefono', 'email', ('ha_sido_condenado_o_detenido', 'motivo'), 'industrial',  'contratado',  'observaciones' ,)}),
       # ('Información personal', {'fields': ()}),
       # ('Información de contacto', {'fields': ()}),
       # ('Otros', {'fields': (  
       #  ) }),
         #('fecha_contratacion', 'instalacion')#
    )


class ContratadoAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombres', 'apellidos', 'fecha_contratacion', 'instalacion', 'fecha_de_nacimiento', 'os10', 'vencimiento', )
    fieldsets = (
    ('', {'fields':('nombres', 'apellidos', 'fecha_de_nacimiento', ('os10', 'vencimiento'), 'instalacion')}),
     
    )
    list_filter = ('os10', 'fecha_contratacion')

admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Instalacion)
#admin.site.register(Contratado)
admin.site.register(Supervisor)
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Medio)

admin.site.register(Contratado, ContratadoAdmin)
