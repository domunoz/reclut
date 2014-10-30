from django.contrib import admin
from models import *
# Register your models here.
class PostulanteAdmin(admin.ModelAdmin):
    list_display= ('fecha', 'rut', 'nombres', 'apellidos',  'comuna', 'email', 
       'os10', 'sexo', 'medio', 'cargo', 'telefono', 'contratado' )
    list_filter =  ('comuna', 'os10', 'sexo','medio', 'cargo', )


admin.site.register(Postulante, PostulanteAdmin)
#admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Cargo)
admin.site.register(Medio)


