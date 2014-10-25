# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postulantes', '0007_auto_20141025_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulante',
            name='creado_por',
            field=audit_log.models.fields.CreatingUserField(editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postulante',
            name='afp',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name=b'AFP', choices=[(b'PR', b'Provida'), (b'HA', b'Habitat'), (b'CA', b'Capital'), (b'MO', b'Modelo'), (b'CU', b'Cuprum'), (b'PV', b'Planvital')]),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='rut',
            field=models.CharField(help_text=b'ej: 15774223-2', max_length=20, null=True, verbose_name=b'RUT', blank=True),
        ),
    ]
