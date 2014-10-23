# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('rut', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=140)),
                ('apellidos', models.CharField(max_length=140)),
                ('domicilio', models.CharField(max_length=140)),
                ('telefono', models.CharField(max_length=140)),
                ('sexo', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('os10', models.BooleanField(default=False)),
                ('observaciones', models.TextField(max_length=140)),
                ('cargo', models.ForeignKey(to='postulantes.Cargo')),
                ('comuna', models.ForeignKey(to='postulantes.Comuna')),
                ('medio', models.ForeignKey(to='postulantes.Medio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(to='postulantes.Region'),
            preserve_default=True,
        ),
    ]
