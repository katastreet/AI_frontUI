# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-01 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=None, verbose_name='date asked'),
        ),
    ]