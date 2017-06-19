"""
WSGI config for fix project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
from whitenoise.django import DjangoWhiteNoise

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fix.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
