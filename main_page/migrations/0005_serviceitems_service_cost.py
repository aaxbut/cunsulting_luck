# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_auto_20160615_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitems',
            name='service_cost',
            field=models.IntegerField(default=0),
        ),
    ]
