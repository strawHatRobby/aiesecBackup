# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-18 18:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('review_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_by', to=settings.AUTH_USER_MODEL)),
                ('review_of', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='review_of', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
