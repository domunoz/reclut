# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0003_remove_postulante_comuna2'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulante',
            name='escolaridad',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'B', b'B\xc3\xa1sica'), (b'M', b'Media')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'S', b'Soltero'), (b'C', b'Casado'), (b'SE', b'Separado'), (b'V', b'Viudo')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='fecha_de_nacimiento',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='hijos',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='telefono_emergencia',
            field=models.CharField(max_length=140, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postulante',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
        ),
    ]
