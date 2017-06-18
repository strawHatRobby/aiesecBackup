from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
class Review(models.Model):
    review_of = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='review_of')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    added_on = models.DateTimeField(auto_now_add=True)
    review_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                related_name='reviewed_by')
