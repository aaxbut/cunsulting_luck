# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 16:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_page', '0015_auto_20160718_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog_subject', models.CharField(max_length=250)),
                ('blog_message', models.TextField()),
                ('blog_is_deploy', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='servicecart',
            name='service_in_cart',
            field=models.ManyToManyField(related_name='servincart', to='main_page.ServiceItems'),
        ),
    ]
