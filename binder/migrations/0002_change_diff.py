# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-08 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='change',
            name='diff',
            field=models.BooleanField(default=False),
        ),
    ]