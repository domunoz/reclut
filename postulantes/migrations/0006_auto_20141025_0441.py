# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0005_auto_20141025_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulante',
            name='ha_sido_condenado_o_detenido',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='industrial',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='motivo',
            field=models.CharField(max_length=140, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='retail',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='vencimiento',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postulante',
            name='rut',
            field=models.CharField(help_text=b'ej: 15774223-2', max_length=140, null=True, verbose_name=b'RUT', blank=True),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='telefono',
            field=models.CharField(max_length=140, null=True, verbose_name=b'tel\xc3\xa9fono', blank=True),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='telefono_emergencia',
            field=models.CharField(max_length=140, null=True, verbose_name=b'tel\xc3\xa9fono emergencia', blank=True),
        ),
    ]
