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

    def get_dept_name(self):
        return '{}'.format(self.name)
        
    def __str__(self):
        return '{}'.format(self.name)
