from .base import *
import environ

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['www.redsleeves.co.uk', 'redsleeves.co.uk','red-skin-syndrome.onrender.com']

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'RedSleeves'
# EMAIL_BACKEND =  'django.core.mail.backends.smtp.EmailBackend'

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


print("PGDATABASE:", env('PGDATABASE', default="Not set"))
print("PGUSER:", env('PGUSER', default="Not set"))
print("PGPASSWORD:", env('PGPASSWORD', default="Not set"))
print("PGHOST:", env('PGHOST', default="Not set"))
print("PGSSLMODE:", env('PGSSLMODE', default="Not set"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('PGDATABASE'),
        'USER': env('PGUSER'),
        'PASSWORD': env('PGPASSWORD'),
        'HOST': env('PGHOST'),
        'PORT': '5432',  
        'OPTIONS': {
            'sslmode': env('PGSSLMODE'),
        },
    }
}
