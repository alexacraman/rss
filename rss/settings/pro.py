from .base import *
import os



SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['www.redsleeves.co.uk', 'redsleeves.co.uk', 'redsleeves.herokuapp.com']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'RedSleeves <acramanalex@gmail.com>'
EMAIL_BACKEND =  'django.core.mail.backends.smtp.EmailBackend'


MANAGERS = (
    ('Alex Acraman','acramanalex@gmail.com' )
)


CORS_REPLACE_HTTPS_REFERER      = True
# HOST_SCHEME                     = "https://"
# SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_HSTS_PRELOAD             = True
SECURE_FRAME_DENY               = True
SECURE_CONTENT_TYPE_NOSNIFF     = True
SECURE_BROWSER_XSS_FILTER       = True
# X_FRAME_OPTIONS                 = True