# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0004_postulante_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulante',
            name='contratado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
