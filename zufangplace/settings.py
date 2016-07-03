# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from os.path import dirname, abspath, join

try:
    from envelop import Environment
except ImportError:
    raise ImportError('could not import envelop, please make sure it is installed (pip install envelop)')

env = Environment()

PRODUCTION = env.get_bool("PRODUCTION", False)
ADMIN = env.get_bool("ADMIN", False)

LOCAL_FILE = lambda *parts: join(abspath(dirname(__file__)), *parts)

DEBUG = not PRODUCTION
TEMPLATE_DEBUG = DEBUG

SITE_DOMAIN = env.get('SITE_DOMAIN', '127.0.0.1:8000')

SECURE_DOMAIN = env.get_bool('SECURE_DOMAIN', False)

if SECURE_DOMAIN:
    PROTOCOL = "https"
else:
    PROTOCOL = "http"


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

db_auth = env.get_uri('DATABASE_DEFAULT', "postgresql://test@localhost/test_zufangplace")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_auth.path.replace('/', ''),
        'HOST': db_auth.host,
        'PORT': db_auth.port,
        'USER': db_auth.user,
        'PASSWORD': db_auth.password,
    },
}

INTERNAL_IPS = ('127.0.0.1',)

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = env.get('STATIC_URL', '/static/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# use some kind of cdn
# MEDIA_URL =

SECRET_KEY = env.get('SECRET_KEY', 'secret_key')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

template_tuple = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

if DEBUG:
    TEMPLATE_LOADERS = template_tuple
else:
    # Only cache the templates outside of DEBUG
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', template_tuple),
    )


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'zufangplace.urls'
WSGI_APPLICATION = 'zufangplace.wsgi.application'

TEMPLATE_DIRS = (
    LOCAL_FILE('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',
)

import jinja2

jinja_cache = jinja2.FileSystemBytecodeCache()

JINJA2_ENVIRONMENT_OPTIONS = {
    'autoescape': True,
    'auto_reload': False,
    'cache_size': -1,
    'bytecode_cache': jinja_cache,
    'undefined': jinja2.StrictUndefined,
}

if DEBUG:
    # Set no cache locally so that template changes will automatically reload
    # without needing to restart runserver.
    JINJA2_ENVIRONMENT_OPTIONS['cache_size'] = 0


INSTALLED_APPS = (
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Third-party
    'raven.contrib.django.raven_compat',

    # Our own apps
    'zufangplace.zufang',
    'rest_framework',
)


# Cookie keys must be byte-strings
SESSION_ENGINE = env.get('SESSION_ENGINE', 'django.contrib.sessions.backends.file')

SESSION_COOKIE_DOMAIN = None

SESSION_COOKIE_AGE = 15552000  # 6 month session expiration

SESSION_COOKIE_NAME = b'sessionid'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

DEFAULT_LOGGER_DICT = {
    'handlers': ['sentry_handler'],
    'level': 'INFO',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'sentry_handler': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        'default': DEFAULT_LOGGER_DICT,
    }
}

RAVEN_CONFIG = {'dsn': env.get('RAVEN_DSN')}

TEST_RUNNER = 'unclebob.runners.Nose'

THIRTY_MINUTES = 60 * 30

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': THIRTY_MINUTES,
    }
}
