#coding:utf-8
from django.db import models


class Region(models.Model):
    nombre = models.CharField(max_length=140)
    
    def __unicode__(self):
        return self.nombre 


class Comuna(models.Model):
    nombre = models.CharField(max_length=140)
    region = models.ForeignKey(Region)
     
    def __unicode__(self):
        return self.nombre 

    class Meta:
        ordering = ('nombre', )


class Medio(models.Model):
    nombre = models.CharField(max_length=140)
 
    def __unicode__(self):
        return self.nombre 


class Cargo(models.Model):
    nombre = models.CharField(max_length=140)
    def __unicode__(self):
        return self.nombre 

  
class Postulante(models.Model):
    fecha = models.DateField( null=True, blank=True)
    rut = models.CharField(max_length=140, primary_key=True)
    nombres = models.CharField(max_length=140)
    apellidos = models.CharField(max_length=140)
    domicilio = models.CharField(max_length=140)
    comuna = models.CharField(max_length=140)
    os10 = models.BooleanField('OS-10', default=False)
    sexo = models.CharField(max_length=140 )
    medio = models.CharField(max_length=140)
    cargo = models.CharField(max_length=140)
    telefono = models.CharField(max_length=140)
    observaciones = models.TextField()
    
    def __unicode__(self):
        return "%s %s"%(self.nombres, self.apellidos)

    class Meta:
        ordering = ('-fecha', )
