# for now fetch the development settings only
from .development import *

import os
from pathlib import Path
# turn off all debugging
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# You will have to determine, which hostnames should be served by Django
# ALLOWED_HOSTS = ["*"]
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / 'run' / 'static'
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / 'run' / 'media'
# ##### SECURITY CONFIGURATION ############################
CSRF_TRUSTED_ORIGINS = ["http://localhost:1337", "https://cuetsarthi.com", 'http://192.168.29.59:1337']
# TODO: Make sure, that sensitive information uses https
# TODO: Evaluate the following settings, before uncommenting them
# redirects all requests to https
# SECURE_SSL_REDIRECT = True
# session cookies will only be set, if https is used
# SESSION_COOKIE_SECURE = True
# how long is a session cookie valid?
# SESSION_COOKIE_AGE = 1209600
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "run" / "dev.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
# validates passwords (very low security, but hey...)
AUTH_PASSWORD_VALIDATORS = [
   { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
   { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
   { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
   { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# the email address, these error notifications to admins come from
SERVER_EMAIL = 'root@localhost'

# how many days a password reset should work. I'd say even one day is too long
PASSWORD_RESET_TIMEOUT_DAYS = 1
