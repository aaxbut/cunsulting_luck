# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-15 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0011_auto_20160715_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecart',
            name='service_in_cart',
            field=models.ManyToManyField(null=True, to='main_page.ServiceItems'),
        ),
    ]