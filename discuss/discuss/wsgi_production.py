"""
Production WSGI config for discuss project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "discuss.discuss.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
