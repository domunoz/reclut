#coding:utf-8
from django.contrib import admin
from models import Postulante, Instalacion, Contratado
# Register your models here.
class PostulanteAdmin(admin.ModelAdmin):
    list_display= ( 'fecha','nombres', 'apellidos',  'comuna', 
             'contratado',  'observaciones', 'medio',  )
    list_filter =  (  'contratado',  'fecha', 'comuna')
#    list_editable = ('ha_sido_condenado_o_detenido',)

#    radio_fields = {'sexo': admin.VERTICAL, 'escolaridad': admin.HORIZONTAL }

    search_fields = ('nombres', 'apellidos',) 
    fieldsets = (
        ('', {'fields': ('fecha', 'medio', 'nombres','apellidos', 'domicilio', 'comuna',
         'ubicacion',  'telefono', 'email', 'contratado',  'observaciones' ,)}),
       # ('Información personal', {'fields': ()}),
       # ('Información de contacto', {'fields': ()}),
       # ('Otros', {'fields': (  
       #  ) }),
         #('fecha_contratacion', 'instalacion')#
    )


class ContratadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'fecha_contratacion', 'instalacion', 'fecha_de_nacimiento', 'os10', 'vencimiento', )
    fieldsets = (
    ('', {'fields':('nombres', 'apellidos', 'fecha_de_nacimiento', ('os10', 'vencimiento'), 'instalacion')}),
     
    )
    list_filter = ('os10', 'fecha_contratacion')

admin.site.register(Postulante, PostulanteAdmin)
#admin.site.register(Instalacion)
#admin.site.register(Contratado, ContratadoAdmin)
