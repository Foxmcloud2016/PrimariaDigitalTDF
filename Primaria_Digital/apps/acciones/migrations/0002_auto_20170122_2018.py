# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accion',
            name='comentarios',
            field=models.TextField(default=None, null=True),
        ),
    ]
