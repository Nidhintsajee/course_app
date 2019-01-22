# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-07 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20190107_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(default=1, max_length=140, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=('category_name',), unique=True, verbose_name='category_slug'),
        ),
    ]