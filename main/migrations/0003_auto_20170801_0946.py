# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-01 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_question_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateField(default=None, verbose_name='date asked'),
        ),
    ]