# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-18 19:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_of', to=settings.AUTH_USER_MODEL),
        ),
    ]
