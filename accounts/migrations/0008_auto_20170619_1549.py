# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-19 10:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170619_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid email', message=b'Email must end with @aiesec.net', regex=b'^[a-z0-9](\\.?[a-z0-9]){5,}@aiesec\\.net$')]),
        ),
    ]