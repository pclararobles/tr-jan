"""
Django settings picked when running in local/dev.
"""
from os import environ  # noqa

from .base import *  # noqa


# GENERAL
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = ["*"]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": (f"redis://redis" f":6379" f"/3"),  # noqa
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}


LOGGING = {
    "version": 1,
    "loggers": {
        "cleverea_logger": {
            "level": "DEBUG" if int(environ.get("DEBUG", "0")) else "INFO",
            "propagate": False,
        }
    },
}

STACK = "staging"
