"""
ASGI config for coursemanager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""
# importing os module.
import os

# This is imported to get ASGI application callable.
from django.core.asgi import get_asgi_application

#setting the default settings module for the project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')

# getting the ASGI application callable that will be used by the ASGI server to forward requests to.
application = get_asgi_application()
