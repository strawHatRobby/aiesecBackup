from __future__ import unicode_literals
from django.conf import settings
from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to=user_directory_path)
    description = models.TextField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, related_name="uploader")
