"""
WSGI config for dimawebapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
import os
import sys


path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "dimawebapp.settings"
application = get_wsgi_application()

application = WhiteNoise(application, root=os.path.join(path, 'resources'))
# application.add_files("/path/to/more/static/files", prefix="more-files/")
