# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adm',
            name='anio_recepcion',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]