import sys
import os



# Absolute paths for where the project and templates are stored.
ABSOLUTE_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
ABSOLUTE_TEMPLATES_PATH = '%s/templates' % ABSOLUTE_PROJECT_ROOT


# add root directory to PYTHONPATH
if not ABSOLUTE_PROJECT_ROOT in sys.path:
    sys.path.insert(0, ABSOLUTE_PROJECT_ROOT)
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

STATIC_ROOT = '%s/static-collected' % ABSOLUTE_PROJECT_ROOT

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = '%s/media' % ABSOLUTE_PROJECT_ROOT

# The URL that handles the media, static, etc.
STATIC_URL = '/static/'
MEDIA_URL = STATIC_URL + 'media/'

# Additional locations of static files
STATICFILES_DIRS = (
    '%s/static-assets' % ABSOLUTE_PROJECT_ROOT,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = "ypnoz^web)wfs_+d7ghv0s54_44zilyof9+n=mf-2t%v2e6=+m"
#Probably add other devs too

ADMINS = (
    ('Cameron Poole', 'Cameron.Poole@health.wa.gov.au'),
)

MANAGERS = ADMINS

# Absolute paths for where the project and templates are stored.
ABSOLUTE_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
ABSOLUTE_TEMPLATES_PATH = '%s/templates' % ABSOLUTE_PROJECT_ROOT

# Python dotted path to the WSGI application used by Django's runserver.
# disabled - outsite the app
WSGI_APPLICATION = 'wsgihandler.application'

DATABASES = {
        'default':{
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME':'test_database',
            'USER':'cameronp',
            # I swear I will change that :)
            'PASSWORD':'password123',
            'HOST':'localhost',
            'PORT':''
            }
        }

TIME_ZONE = 'Australia/Perth'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-au'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# APPS
# django debugging stuff
ADMIN_TOOL_APPS = (

    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
)


CORE_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)

EXTERNAL_APPS = ('django_extensions',
                'south',
                'bootstrap3',
                'debug_toolbar',
)

LOCAL_APPS = (
    'DLB_activity_log.home',
)

# the order is important!
INSTALLED_APPS = ADMIN_TOOL_APPS + CORE_APPS + LOCAL_APPS +  EXTERNAL_APPS 

DEBUG = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
