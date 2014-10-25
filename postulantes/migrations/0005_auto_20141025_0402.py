# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0004_auto_20141025_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postulante',
            name='otro',
        ),
        migrations.AddField(
            model_name='postulante',
            name='afp',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'PR', b'Provida'), (b'HA', b'Habitat'), (b'CA', b'Capital'), (b'MO', b'Modelo'), (b'CU', b'Cuprum'), (b'PV', b'Planvital')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='jubilado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postulante',
            name='sistema_de_salud',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'F', b'FONASA'), (b'I', b'ISAPRE')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postulante',
            name='contratado',
            field=models.BooleanField(default=False, verbose_name=b'contratado'),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='os10',
            field=models.BooleanField(default=False, verbose_name=b'OS-10 al d\xc3\xada'),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='rut',
            field=models.CharField(help_text=b'ej: 15774223-2', max_length=140, null=True, verbose_name=b'RUT.', blank=True),
        ),
    ]
