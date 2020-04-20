"""
Base settings to build other settings files upon.
"""

import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('django_q_starter')

# Load operating system environment variables and then prepare to use them
env = environ.Env()
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

if READ_DOT_ENV_FILE:
    # Operating System Environment variables have precedence over variables defined in the .env file,
    # that is to say variables from the .env files will only be used if not defined
    # as environment variables.
    env_file = str(ROOT_DIR.path('.env'))
    print(f'Loading : {env_file}')
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# URLS
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# APPS
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#installed-apps
DJANGO_APPS = [
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'django_q',
]

# Apps specific for this project go here.
LOCAL_APPS = [
    'django_q_starter.email_example.apps.EmailExampleConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

SITE_ID = 1

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.2/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/2.2/ref/settings/#dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# Uses django-environ to accept uri format
# See: https://django-environ.readthedocs.io/en/latest/#supported-types
DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------
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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#language-code
LANGUAGE_CODE = 'zh-Hant'

# See: https://docs.djangoproject.com/en/2.2/ref/settings/#time-zone
TIME_ZONE = 'Asia/Taipei'

# See: https://docs.djangoproject.com/en/2.2/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/2.2/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/2.2/ref/settings/#use-tz
USE_TZ = True

# STATIC FILE (CSS, JavaScript, Images) CONFIGURATION
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/2.2/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]

# See: https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/2.2/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR('uploads'))

# See: https://docs.djangoproject.com/en/2.2/ref/settings/#media-url
MEDIA_URL = '/uploads/'


# SETTINGS FOR EMAILING
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
