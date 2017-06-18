from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Progress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='progress_of')
    quality1 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    quality2 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    quality3 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    quality4 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    quality5 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    quality6 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    quality7 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    quality8 = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
