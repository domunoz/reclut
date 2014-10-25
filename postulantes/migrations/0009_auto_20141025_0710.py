# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0008_auto_20141025_0645'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.RemoveField(
            model_name='comuna',
            name='region',
        ),
        migrations.DeleteModel(
            name='Comuna',
        ),
        migrations.DeleteModel(
            name='Medio',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.AlterField(
            model_name='postulante',
            name='creado_por',
            field=audit_log.models.fields.CreatingUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'ingresado por'),
        ),
    ]
