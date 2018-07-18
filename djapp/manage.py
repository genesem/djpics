#!/usr/bin/python3

# modded version of manage tool used as usual to run/migrate etc
# documentation
# https://docs.djangoproject.com/en/2.0/ref/django-admin/
# basic run: python manage.py runserver localhost:8000


import sys
from os import environ
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
    execute_from_command_line(sys.argv)

