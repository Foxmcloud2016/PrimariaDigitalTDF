# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='directivo',
            field=models.CharField(default='Director/a', max_length=50),
        ),
        migrations.AddField(
            model_name='escuela',
            name='tel_directivo',
            field=models.CharField(default='Numero', max_length=50),
        ),
    ]
