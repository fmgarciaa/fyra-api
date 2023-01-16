"""Development settings."""

from .base import *
from .base import env

# Base
DEBUG = True

# Security
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="0525cLHQ1YYprdxq8Q47OkMJmOK2zEr2gzEIaXWtNE2RTf7T2XLDcpDcE3d2JBen",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# CACHES
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# EMAIL
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = 1025


# django-extensions
INSTALLED_APPS += ["django_extensions"]

# Celery
CELERY_TASK_EAGER_PROPAGATES = True
