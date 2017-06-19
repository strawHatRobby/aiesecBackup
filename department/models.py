from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255,unique=True,blank=False)
    info = models.TextField(max_length=500, blank=True)



    @models.permalink
    def get_absolute_url(self):
        return 'department:home', (self.slug,)

# class Moderator(models.Model):
#     department = models.OneToOneField(Department, on_delete=models.CASCADE,
#                                         related_name="department_of")
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
#                                 related_name="moderator_of")
