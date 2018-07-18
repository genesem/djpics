# WSGI config for your project.
# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/

# this version is modded


from os import environ
from django.apps import apps
from django.conf import settings
from django.utils.log import configure_logging
from django.core.handlers.wsgi import WSGIHandler

environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
apps.populate(settings.INSTALLED_APPS)
app = WSGIHandler()
