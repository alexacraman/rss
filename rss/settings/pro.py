from .base import *
import environ
from pathlib import Path

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['www.redsleeves.co.uk', 'redsleeves.co.uk', 'red-skin-syndrome.onrender.com']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'RedSleeves <acramanalex@gmail.com>'
EMAIL_BACKEND =  'django.core.mail.backends.smtp.EmailBackend'

MANAGERS = (
    ('Alex Acraman','acramanalex@gmail.com' )
)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_AGE              = 86400 # delete the session cookie after on
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_HSTS_PRELOAD             = True

SESSION_COOKIE_SECURE           = True #Set this to True to avoid transmitting the session cookie over HTTP accidentally.
CSRF_COOKIE_SECURE              = True #Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
SECURE_SSL_REDIRECT             = False

import dj_database_url
DATABASES['default'] = dj_database_url.config(
    default=env("DATABASE_URL"),
    conn_max_age=600,
    conn_health_checks=True,
)
# DATABASE_URL = env('DATABASE_URL')
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "postgresql_rss",
#         "USER": "postgresql_rss",
#         "PASSWORD": env('PASSWORD'),
#         "HOST": env("HOST"),
#         "PORT": "5432",
#     }
# }