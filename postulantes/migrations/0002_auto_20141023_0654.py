# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postulantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comuna',
            options={'ordering': ('nombre',)},
        ),
        migrations.AddField(
            model_name='postulante',
            name='fecha',
            field=models.CharField(max_length=140, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postulante',
            name='cargo',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='comuna',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='medio',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='observaciones',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='os10',
            field=models.BooleanField(default=False, verbose_name=b'OS-10'),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='rut',
            field=models.CharField(max_length=140, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='sexo',
            field=models.CharField(max_length=140),
        ),
    ]
