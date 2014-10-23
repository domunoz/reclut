from django.contrib import admin
from models import *
# Register your models here.
class PostulanteAdmin(admin.ModelAdmin):
    list_display= ('fecha', 'rut', 'nombres', 'apellidos', 'domicilio', 'comuna', 
       'os10', 'sexo', 'medio', 'cargo', 'telefono' )
    list_filter =  ('comuna', 'os10', 'sexo','medio', 'cargo', )


admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Cargo)
admin.site.register(Medio)


