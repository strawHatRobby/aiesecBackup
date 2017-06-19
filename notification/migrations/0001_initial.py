# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-19 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
