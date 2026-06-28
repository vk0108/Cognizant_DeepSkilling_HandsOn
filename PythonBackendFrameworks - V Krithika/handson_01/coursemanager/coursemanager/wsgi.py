"""
WSGI config for coursemanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""
#importing os module.
import os

# This is imported to get WSGI application callable.
from django.core.wsgi import get_wsgi_application

#setting the default settings module for the project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')

# getting the WSGI application callable that will be used by the WSGI server to forward requests to.
application = get_wsgi_application()
