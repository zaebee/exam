import os, sys

from genericpath import isfile

ugettext = lambda s: s

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

sys.path.insert(0, rel('apps'))

INTERNAL_IPS = ('127.0.0.1')
DEFAULT_CHARSET = 'utf-8'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('zaebee', 'sinezub@yandex.ru'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('develop.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SERVER_EMAIL = 'errors@proj.local'

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en', ugettext('English')),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = rel('media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel('static')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_DIRS = (
    rel('templates')
)

STATICFILES_DIRS = (
    rel('static'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    #'django.contrib.staticfiles',

    'south',
    'dynamic_models',

)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': rel('tmp/django_cache'),
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}



if isfile(rel('settings_local.py')):
    from settings_local import *
if isfile(rel('local_settings.py')):
    from local_settings import *
