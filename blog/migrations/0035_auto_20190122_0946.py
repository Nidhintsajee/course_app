# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-22 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20190121_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='status',
            field=models.CharField(choices=[('User', 'User'), ('Admin', 'Admin')], default='User', max_length=200),
        ),
    ]
