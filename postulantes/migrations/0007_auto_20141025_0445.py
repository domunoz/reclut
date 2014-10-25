# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0006_auto_20141025_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulante',
            name='visto_bueno',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postulante',
            name='contratado',
            field=models.BooleanField(default=False),
        ),
    ]
