# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-07 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20190107_1030'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]