# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-19 06:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20170618_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-added_on',)},
        ),
        migrations.AlterField(
            model_name='review',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]