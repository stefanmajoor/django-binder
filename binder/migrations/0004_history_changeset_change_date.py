# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-14 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binder', '0003_history_remove_reverse_spam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changeset',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]