# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0002_postulante_otro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postulante',
            name='comuna2',
        ),
    ]
