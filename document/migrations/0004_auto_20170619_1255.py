# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-19 07:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20170619_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to=settings.AUTH_USER_MODEL),
        ),
    ]
