# coding=utf-8

from __future__ import absolute_import
from .base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

VAR_DIR = normpath(join(SITE_ROOT, '..', 'var'))

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025


# Override
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        # Log to a text file that can be rotated by logrotate
        # the log path should be generated before run
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'simple',
            'filename': normpath(join(VAR_DIR, 'log', 'django',
                                      'server.log')),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'server': {
            'handlers': ['logfile'],
            'level': 'WARNING',  # Or maybe INFO or DEBUG
            'propagate': False
        },
        'accblacksmith': {
            'handlers': ['logfile'],
            'level': 'WARNING',  # Or maybe INFO or DEBUG
            'propagate': False
        },
        'tinyurl': {
            'handlers': ['logfile'],
            'level': 'WARNING',  # Or maybe INFO or DEBUG
            'propagate': False
        },
        'handsetcare': {
            'handlers': ['logfile'],
            'level': 'WARNING',  # Or maybe INFO or DEBUG
            'propagate': False
        },
        'predup': {
            'handlers': ['logfile'],
            'level': 'WARNING',  # Or maybe INFO or DEBUG
            'propagate': False
        },
        'common': {
            'handlers': ['logfile'],
            'level': 'INFO',  # Or maybe INFO or DEBUG
            'propagate': False
        },
    },

}

# local db
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "lolstat",
        "USER": "test",
        "PASSWORD": "test",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# test release server
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql", # postgresql_psycopg2 is old name
#         "NAME": "server",    # DB name
#         "USER": "django",
#         "PASSWORD": "djangoserver",
#         "HOST": "133.130.118.56",
#         "PORT": "5432",
#     }
# }



INSTALLED_APPS += []
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE += \
    []


ENCRYPT_PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAv0mUaGJoed0dyZYQhVhMiW8mNzwZ4f8gbXERYExOmoOu+8g8\nLJuDpD14g4jxMPaOq5ROQSnsv6CpDKCUH8CZSO/5G644N+NVkRt79mwQLZOBbT5Q\nR4nOVFKOTa574X4Hn4nFLXhYUSs/sRqdA/XilaMDOkEvcroqLI8gCKQ8xJeWikCB\nl4+ohiQYx0JkHq5wKC+0yz40G7Cjiz7f6Nuni65wk3LDu1cZ30cM7+si/2GKUBnH\nINHvfCHU3yBZ+VjiS8Z+XqgSPmLBxaO0VEOIhtQFrCJZJl+nBCD2feG0iu0sg5Lf\nKbrqO0MjN/2jY7A5iVHxSvz43tcDFotf6in6WwIDAQABAoIBAGrP+FnNUY9yw/ZT\noEgFRT+c3BcNrVo/rujNsSk3ktC+5U/cwJUcBYcJeCjip+NyWbo/Zu8GLRfX622M\noQmV70IGFfC5+NRkUdxkH3U7ZFE+w4+vsv4vWhJFwwZnfu8sA6+3K243fAFfCAKp\n3LFgdLSfwOafjZIfl/sntHh+1RvknkkwPftjA7NNg/YL1Nb5Ch2DvPB1Hu3AKQnQ\naHoRorf57Pii4WY8upVcDs0vO/wj8gm/uWtvCf570qxfLhcI+C6hDUveE9Z71kMh\nv1tKa2MVqRl3HM7vwm18ee0hcGTWp1e7P01SxUprcEq+nIMD2oV0wSiTIb4429p/\nEssusykCgYEA4vDDBuXrn086jaFihhVIa0f4V9lVH26UwzjuRyXSM4fs2zBDcUm1\nRe50+ZVD9cwNvP0DH4xQjJq0xe84X+hrKsmIYgGQxz3mPItutfrxUR5zkugrG/jA\nbeQ4LxOl10Qs++pr3xdgfT2rjC6h3ey37eIY1jX4towlUcWSuWeOomUCgYEA18gX\nJeWsWl+8iF+xlDb0OQfFEUtauhCDooYHhRDzsRLz7/02beEeTpIwKCZnSRpXBpW1\nTd5qpBMsFxJPnmjh6faKgIhbASAmeH0h/1P4ntUg2dtvJZM4cyhTVqEhxHt/FN9X\nSjhL18S4f7D6ZjlGLC2nS2I3g0famEGGmAqt/b8CgYBsZF5iPxLpRmhLGVf7ftLW\nGsvs+asElkaLb/evF8tsPXHNxyGPTIs+WYSZaMfK8KlnKNmDCfu3DHVnTLj6ZgI5\nr4RqeyDxaQk8xcQdOzxjaE3/TtC4TXlrg2OqaJH/XVq2/+KB7aJybzAuhl9dpiC7\niBAg0Cp41jtE8T8BOwsPWQKBgCC/UxQDSSbmBJzFuRN/S40kKro3L2uxeei+YoHF\nUtZ6w96WFR6T3Z+a/Af73AzyHGb5bWyF5rVD25scwkyOKkrxiY98IiOHl48Nno07\nVy3ztmqZrMKNFzIS2qL5DUDeZSjrxDmVVZ1HU6C9YSMGainmO89q9nXL/9a/iwek\nB0fNAoGAdq9J77YUXOWevwbMdisfF/jgpAWMcdU0xOW8Ir1VCYRCuXyy1DqOUOor\npQGIwr6zXMTItDUqmlZgnZQF3vT7WafWTa+dC+WcZTB+d9NmZ9goknLJQiweXyf7\nP2AOAvQ1jBsRaQ/tWudxG5/3smnvWZYqhxY4qgOy8fYoPVu6TAI=\n-----END RSA PRIVATE KEY-----"
# ENCRYPT_PUBLIC_KEY_PATH = "server/settings/public.key"
SOCIAL_AUTH_FACEBOOK_KEY  = "1663461823892518"
SOCIAL_AUTH_FACEBOOK_SECRET  = "867691ad9871d4cb6715d9fc2ce38154"



### EMAIL CONFIGURATION

# EMAIL_HOST = 'localhost'
# # Port 587 is the default port for smtp submission, but some will use 25, 465, or an arbitrary port #
# EMAIL_PORT = 465
#
#
# EMAIL_USE_TLS = False
# EMAIL_NOREPLY = "noreply@gmail.com"  # Not required, but potentially useful to have defined

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gae'
EMAIL_HOST_PASSWORD = 'pw'

EMAIL_USE_TLS = True
EMAIL_NOREPLY = "noreply@gmail.com"  # Not required, but potentially useful to have defined
### END EMAIL CONFIGURATION

# #### django-registraiton CONFIGURATION
ACCOUNT_ACTIVATION_DAYS=7

# #### END django-registraiton CONFIGURATION



# #### django-page CONFIGURATION
server={
    'SITE_NAME': "Moneyball Stock",
    'SUPPORT_URL_CAFE': "http://cafe.naver.com/moneyballstock",
    'SITE_NAME_ROBO': "Robo Stock",
    'DOMAIN_ROBO': "moneyballstock.com",
}

# #### END django-page CONFIGURATION

# #### Celery CONFIGURATION
DART_AUTH_TOKEN="61ea25ee25bb5bdbdbd045600e809531f13f847c"
XLSX_PATH_DAILY_UPDATE=normpath(join(VAR_DIR, 'update', 'daily_stockprice'))
# #### END Celery CONFIGURATION

# #### Celery CONFIGURATION
## Broker settings.
BROKER_URL = 'amqp://guest:guest@localhost//'

# List of modules to import when celery starts.
# CELERY_IMPORTS = ('predup.tasks', )

## Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_ANNOTATIONS = {'predup.tasks.add': {'rate_limit': '10/s'}}

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'predup.tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
    'add-every-10-minutes': {
        'task': 'predup.tasks.pubAnnPredict',
        'schedule': timedelta(minutes=10),
    },
    'add-every-day': {
        'task': 'mfactors.tasks.kospiK200WdateUpdater',
        'schedule': timedelta(minutes=10),
    },
    
}
# #### END Celery CONFIGURATION


# #### Celery CONFIGURATION
PUBANN_DIR=normpath(join(VAR_DIR, 'pubann',))
PUBANN_RECENT_DIR=normpath(join(PUBANN_DIR, 'recent',))
PUBANN_PAST_ZIP_DIR=normpath(join(PUBANN_DIR, 'pastzip',))

PICKLE_DIR=normpath(join(VAR_DIR, 'pkl',))
# #### END Celery CONFIGURATION
