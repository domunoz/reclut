# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0009_auto_20141025_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulante',
            name='nacionalidad',
            field=models.CharField(default=b'Chilena', max_length=140, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postulante',
            name='fecha',
            field=models.DateTimeField(null=True, verbose_name=b'fecha entrevista', blank=True),
        ),
    ]
