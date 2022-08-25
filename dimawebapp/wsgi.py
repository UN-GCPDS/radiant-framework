"""
WSGI config for dimawebapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'namae.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "namae.settings"

application = get_wsgi_application()
