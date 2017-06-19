# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-19 09:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid email', message=b'Email must end with @gmail.com', regex=b'^[a-z0-9](\\.?[a-z0-9]){5,}@aiesec\\.net$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=40, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid_username', message=b'username must be alphanumeric or contain ., @, +, _', regex=b'^[a-zA-Z0-9.@+_]*$')]),
        ),
    ]
