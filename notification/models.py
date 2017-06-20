from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    content = models.TextField(blank=False)
    added_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    @models.permalink
    def get_absolute_url(self):
        return 'notification:home', (self.slug,)

    def __str__(self):
        return '{}'.format(self.title)