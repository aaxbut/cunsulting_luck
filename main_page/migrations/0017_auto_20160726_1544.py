# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0016_auto_20160720_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servicecart',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
    ]