"""Production settings and globals."""

from __future__ import absolute_import

from os import environ

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

# ##### LOAD VARIABLE FROM JSON
# JSON-based secrets module
import json

with open("beluga/settings/secret.json") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


def get_env_setting(setting):
    """ Get the environment setting or return exception """

    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)
# ##### LOAD VARIABLE FROM JSON


# ######### HOST CONFIGURATION
# See:
# https://docs.djangoproject.com/en/1.9/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ["www.hbwhale.com", ".qtrading.co.kr", "133.130.118.56", ".moneyballstock.com"]
# ######### END HOST CONFIGURATION

# ######### EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.worksmobile.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', 'hb13579!')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', "noreply-beluga@hbwhale.com")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER

EMAIL_NOREPLY = "noreplybeluga@hbwhale.com"  # Not required, but potentially useful to have defined

DEFAULT_FROM_EMAIL = EMAIL_NOREPLY
# ######### END EMAIL CONFIGURATION

# ######### DATABASE CONFIGURATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql", # postgresql_psycopg2 is old name
        "NAME": "beluga",    # DB name
        "USER": "django",
        "PASSWORD": get_secret("DB_PW"),
        "HOST": get_secret("DATABASES_HOST"),
        "PORT": get_secret("PORT"),
    }
}
# ######### END DATABASE CONFIGURATION


# ######### CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#caches
CACHES = {
    'default': {
        # local memory cache
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# ######### END CACHE CONFIGURATION


# ######### SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_secret("SECRET_KEY")
# ######### END SECRET CONFIGURATION

# ######### HTTPS CONFIGURATION
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
# ######### END HTTPS CONFIGURATION

# ######### ENCRYPT CONFIGURATION
ENCRYPT_PRIVATE_KEY = get_secret("PRIVATE_KEY")
# ENCRYPT_PUBLIC_KEY_PATH = get_secret("PUBLIC_KEY_PATH")
# ######### END ENCRYPT CONFIGURATION


# ######### FACEBOOK CONFIGURATION
FACEBOOK_APP_ID = get_secret("FB_APP_ID")
FACEBOOK_APP_SECRET = get_secret("FB_APP_SECRET")

# ######### END FACEBOOK CONFIGURATION




# #### django-registraiton CONFIGURATION
ACCOUNT_ACTIVATION_DAYS=7

# #### END django-registraiton CONFIGURATION

# #### django-page CONFIGURATION
BELUGA={
    'SITE_NAME': "Moneyball Stock",
    'SUPPORT_URL_CAFE': "http://cafe.naver.com/moneyballstock",
    'SITE_NAME_ROBO': "Robo Stock",
    'DOMAIN_ROBO': "moneyballstock.com",
}

# #### END django-page CONFIGURATION




# #### Celery CONFIGURATION
DART_AUTH_TOKEN="1e7bc9e1a09aab8a79dd3e10377fbadad7750b61" # key for corp.
XLSX_PATH_DAILY_UPDATE=normpath(join(VAR_DIR, 'update', 'daily_stockprice'))
# #### END Celery CONFIGURATION

# #### Celery Broker CONFIGURATION
## Broker settings.
CELERY_ROUTES = {
    'mfactors.tasks.kospiK200WdateUpdater': {'queue': 'autoupdate'},
    'mfactors.tasks.stockClosePriceUpdater': {'queue': 'autoupdate'},
    'mfactors.tasks.stockVolumeIpoUpdater': {'queue': 'autoupdate'},
    'mfactors.tasks.factorsUpdater': {'queue': 'autoupdate'},
    'forecast.tasks.esurpriseUpdater': {'queue': 'autoupdate'},
    

    # 'mfactors.tasks.testEmail': {'queue': 'autoupdate'}, # test-celery-email
    #'predup.tasks.add': {'queue': 'autoupdate'},

}

BROKER_URL = 'amqp://guest:guest@localhost//'

# List of modules to import when celery starts.
# CELERY_IMPORTS = ('predup.tasks', )

## Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_ANNOTATIONS = {'predup.tasks.add': {'rate_limit': '10/s'}}

# email to ADMIN when error occurs
CELERY_SEND_TASK_ERROR_EMAILS=True

# http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    # celery's default Time Zone is UTC, but for django it uses the TIME_ZONE of
    # Django, {@see : beluga.settingsbase.py}
    # :see http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
    # Executes every weekday at 15:40(6:40+0:00)
    
    'add-every-day-at-martket-open': {
        'task': 'mfactors.tasks.stockVolumeIpoUpdater',
        'schedule': crontab(hour=9, minute=3, day_of_week='mon,tue,wed,thu,fri'),
    },
    'add-every-day-at-martket-open-yesterday-factors': {
        'task': 'mfactors.tasks.factorsUpdater',
        'schedule': crontab(hour=9, minute=30, day_of_week='mon,tue,wed,thu,fri'),
        # 'args': (16, 16),
    },
    'add-every-day-at-martket-open-yesterday-esurprise': {
        'task': 'forecast.tasks.esurpriseUpdater',
        'schedule': crontab(hour=9, minute=33, day_of_week='mon,tue,wed,thu,fri'),
        # 'args': (16, 16),
    },

    'add-every-day-after-martket-close-stockprice': {
        'task': 'mfactors.tasks.stockClosePriceUpdater',
        'schedule': crontab(hour=16, minute=40, day_of_week='mon,tue,wed,thu,fri'),
        # 'args': (16, 16),
    },
    'add-every-day-after-martket-close': {
        'task': 'mfactors.tasks.kospiK200WdateUpdater',
        'schedule': crontab(hour=16, minute=45, day_of_week='mon,tue,wed,thu,fri'),
        # 'args': (16, 16),
    },

    # test-celery-email
    # 'test-celery-email': {
    #     'task': 'mfactors.tasks.testEmail',
    #     'schedule': crontab()
    #     # 'args': (16, 16),
    # },
}


# #### END Celery Broker CONFIGURATION
