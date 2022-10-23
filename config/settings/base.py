"""
Django settings for application project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from os import environ
from os.path import abspath, dirname, join
from typing import List


def root(*dirs: str):
    """
    Joins the BASE_DIR with any specified dir.
    """
    base_dir = join(dirname(__file__), "..", "..")

    return abspath(join(base_dir, *dirs))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

DEBUG = True

BASE_DIR = root()

# GENERAL
# ------------------------------------------------------------------------------
APPS_DIR = root("recerca")

SECRET_KEY = environ.get("DJANGO_SECRET_KEY", "spw9i$9!lwc3!l0^8(1=7aag!pn5r*0wa_4$tllbuu8_8e+8e")
# https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS: List[str] = []
# https://docs.djangoproject.com/en/2.2/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/2.2/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/2.2/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/2.2/ref/settings/#use-tz
USE_TZ = True

TIME_ZONE = "UTC"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/2.2/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"


# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]
THIRD_PARTY_APPS = [
    "corsheaders",
    "django_extensions",
    "drf_spectacular",
    "rest_framework",
]
LOCAL_APPS = [
    "recerca.core.apps.CoreConfig",
]


# https://docs.djangoproject.com/en/2.2/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ.get("PSQL_DB_DATABASE", "recerca"),
        "USER": environ.get("PSQL_DB_USERNAME", "postgres"),
        "PASSWORD": environ.get("PSQL_DB_PASSWORD", "password"),
        "HOST": environ.get("PSQL_DB_HOST", "localhost"),
        "PORT": environ.get("PSQL_DB_PORT", "5432"),
    },
}


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 9},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Default login url when accessing the backoffice
LOGIN_URL = "/recerca/admin/login/"


# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# https://docs.djangoproject.com/en/2.2/ref/settings/#static-root
STATIC_ROOT = join(BASE_DIR, "recerca/static/")
# https://docs.djangoproject.com/en/2.2/ref/settings/#static-url
STATIC_URL = "/recerca/static/"
# https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [root("static")]


# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#media-root
MEDIA_ROOT = root("tmp")
# https://docs.djangoproject.com/en/2.2/ref/settings/#media-url
MEDIA_URL = "/tmp/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [join(APPS_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#middleware


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Django REST framework
# ------------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
    "DATETIME_INPUT_FORMATS": [
        "%Y-%m-%d",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f%z",
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_THROTTLE_RATES": {"user": "1000/day"},  # This value is ignored in the library
    "DEFAULT_SCHEMA_CLASS": "cleverea_django_integrations.swagger.custom_classes.auto_schema.CustomAutoSchema",  # noqa
}

# Drf-spectacular setting to enable binary description for FieldFiles in request schemas
SPECTACULAR_SETTINGS = {"COMPONENT_SPLIT_REQUEST": True}


# Cache configuration.
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}
# REDIS cache URL for health check.
REDIS_URL = environ.get("REDIS_URL", "redis://redis:6379")