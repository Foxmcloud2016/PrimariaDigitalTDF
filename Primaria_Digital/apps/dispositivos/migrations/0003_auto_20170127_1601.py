# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0002_adm_anio_recepcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='adm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dispositivos.Adm'),
        ),
    ]
