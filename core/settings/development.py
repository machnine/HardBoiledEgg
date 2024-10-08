"""devlopment settings"""

# pylint: disable=wildcard-import, unused-wildcard-import
from .base import *  # noqa: F403
import sys

# Debug mode
DEBUG = True

# Secret key for development
SECRET_KEY = "django-insecure-#^_@z!"

ALLOWED_HOSTS = ["*"]
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = "Lax"

# Internal IPs
INTERNAL_IPS = ["127.0.0.1"]

# Installed apps
INSTALLED_APPS += [  # noqa: F405
    "debug_toolbar",
    "django_extensions",
]

# middlewares
MIDDLEWARE += [  # noqa: F405
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Logging for development
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "WARNING",
        },
    },
}

# pretty print in shell_plus (django-extensions) or shell
if "shell" in sys.argv:
    from rich import pretty, inspect

    pretty.install()

    def inspector(obj):
        inspect(obj, methods=True)
