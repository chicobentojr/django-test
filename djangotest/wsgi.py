"""
WSGI config for djangotest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest.settings")

application = get_wsgi_application()

ENV = os.environ.get('ENV', 'Development')

if ENV == 'Production':
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)
