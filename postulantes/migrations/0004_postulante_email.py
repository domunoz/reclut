# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0003_auto_20141030_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulante',
            name='email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
    ]
