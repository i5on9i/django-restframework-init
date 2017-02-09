"""Common settings and globals.
Based on Django 1.10
"""


from os.path import abspath, basename, dirname, join, normpath
import socket
from sys import path


# #### PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))
DJANGO_ROOT = BASE_DIR

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)

# var directory name
VAR_DIR = normpath(join(SITE_ROOT, '..', '..', 'var'))
# #### END PATH CONFIGURATION


# ##### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False


# #### END DEBUG CONFIGURATION


# ##### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Namh', 'cto@hbwhale.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# #### END MANAGER CONFIGURATION


# #### DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
# #### END DATABASE CONFIGURATION

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# #### GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Asia/Seoul'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# #### END GENERAL CONFIGURATION


# #### MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# #### END MEDIA CONFIGURATION


# #### STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))   # for final deploy

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),    # dirs to be searched
)

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# #### END STATIC FILE CONFIGURATION


# #### SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"{{ secret_key }}"
# #### END SECRET CONFIGURATION


# #### SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
# #### END SITE CONFIGURATION


# #### FIXTURE CONFIGURATION
# See:
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
# #### END FIXTURE CONFIGURATION

# #### AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

]
# #### END AUTHENTICATION CONFIGURATION

# #### TEMPLATE CONFIGURATION

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
# TEMPLATE_DEBUG = DEBUG

# See : https://docs.djangoproject.com/en/1.8/ref/settings/#templates
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [normpath(join(SITE_ROOT, 'templates'))],
    'APP_DIRS': True,
    'OPTIONS': {
        'debug': DEBUG,
        # see : https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
        ],
        # Pyjade
        # 'loaders': [
        #     # ('django.template.loaders.cached.Loader', [
        #     #     'django.template.loaders.filesystem.Loader',
        #     #     'django.template.loaders.app_directories.Loader',
        #     # ]),
        #     ('pyjade.ext.django.Loader',(
        #         'django.template.loaders.filesystem.Loader',
        #         'django.template.loaders.app_directories.Loader',
        #     )),
        # ],
        # 'builtins': ['pyjade.ext.django.templatetags'],


    },

}]


# #### END TEMPLATE CONFIGURATION


# #### MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE = [
    # Default Django middleware.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# #### END MIDDLEWARE CONFIGURATION


# #### URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
# #### END URL CONFIGURATION


# #### APP CONFIGURATION
DJANGO_APPS = [
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin panel and documentation:
    'django.contrib.admin',
    

    # Useful template tags:
    # 'django.contrib.humanize',

    'rest_framework',
    # 'rest_framework.authtoken',  # to use TokenAuthentication

]

# Apps specific for this project go here.
LOCAL_APPS = [
    'riotapi',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
# #### END APP CONFIGURATION


# LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to s#### end an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
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
            'formatter': 'verbose',
            'filename': normpath(join(VAR_DIR, 'log', 'django',
                                      'server.log')),
        },
    },
    'loggers': {
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,  # True menasn that the the error messages are passed to the parent hierarchy, i.e. django
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'common': {
            'handlers': ['logfile'],
            'level': 'INFO',  # WARNING means 'warning' level or higher level
            'propagate': False
        },
    },

}
# #### END LOGGING CONFIGURATION


# #### WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
# #### END WSGI CONFIGURATION


# #### REST_FRAMEWORK CONFIGURATION
# See: http://www.django-rest-framework.org/#installation
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    #     'rest_framework.permissions.IsAuthenticated',
    # ],

    # See : http://getblimp.github.io/django-rest-framework-jwt/
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
# #### END REST_FRAMEWORK CONFIGURATION


# #### LOGIN CONFIGURATION
from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('acc:login')

LOGIN_REDIRECT_URL = reverse_lazy('services.mfactor')
REMIT_PASSWORD_RESET_TIMEOUT_DAYS = 2
REMIT_PASSWORD_RESET_TIMEOUT_MINS = 20
# #### END LOGIN CONFIGURATION

# #### SOCIAL AUTH CONFIGURATION
# see : http://psa.matiasaguirre.net/docs/pipeline.html#authentication-pipeline
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',

    # 'accblacksmith.views.require_email',
    #
    # 'social.pipeline.mail.mail_validation',
    'social.pipeline.social_auth.associate_by_email',

    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)
SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    'social.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social.pipeline.disconnect.disconnect',
)

SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'accblacksmith.views.sendVerificationEmail'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/acc/email-verify/'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email',
}
# #### END SOCIAL AUTH CONFIGURATION



# #### Celery CONFIGURATION
PUBANN_DIR=normpath(join(VAR_DIR, 'pubann',))
PUBANN_RECENT_DIR=normpath(join(PUBANN_DIR, 'recent',))
PUBANN_PAST_ZIP_DIR=normpath(join(PUBANN_DIR, 'pastzip',))

PICKLE_DIR=normpath(join(VAR_DIR, 'pkl',))
# #### END Celery CONFIGURATION




