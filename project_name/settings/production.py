# -*- coding: utf-8 -*-

"""Production settings and globals."""

from .common import *

########## DATABASE CONFIGURATION
DATABASE = {
    'NAME': 'DB_NAME',
    'USER': 'DB_USER',
    'PASSWORD': 'DB_PASS'
}
########## END DATABASE CONFIGURATION

########## ALLOWED HOSTS
ALLOWED_HOSTS = []

########## END ALLOWED HOSTS


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.gmail.com'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = ''

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = ''

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 587

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE.get('NAME'),
        'USER': DATABASE.get('USER'),
        'PASSWORD': DATABASE.get('PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
########## END CACHE CONFIGURATION


########## STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    
)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'



STATIC_ROOT = '/home/WF_USER/webapps/{{ project_name }}_static/'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static' 
########## END STORAGE CONFIGURATION


########## GENERIC CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#prepend-www
PREPEND_WWW = True
########## GENERIC CONFIGURATION


THUMBNAIL_DEFAULT_STORAGE = STATICFILES_STORAGE


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    # 'debug_toolbar',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE += (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)
########## END TOOLBAR CONFIGURATION


# def custom_show_toolbar(request):
#     return True  # Always show toolbar, for example purposes only.

# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
#     'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar
# }
