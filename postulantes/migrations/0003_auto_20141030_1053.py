# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0002_auto_20141023_0654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postulante',
            options={'ordering': ('-fecha',)},
        ),
        migrations.AlterField(
            model_name='postulante',
            name='fecha',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='telefono',
            field=models.CharField(max_length=140, null=True, blank=True),
        ),
    ]
