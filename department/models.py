from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255,unique=True,blank=False)


# class Moderator(models.Model):
#     department = models.OneToOneField(Department, on_delete=models.CASCADE,
#                                         related_name="department_of")
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
#                                 related_name="moderator_of")
