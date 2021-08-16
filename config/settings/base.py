"""
Base settings to build other settings files upon.
"""
from pathlib import Path

import environ


ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = ROOT_DIR / 'django_q_starter'

# Load operating system environment variables and then prepare to use them
env = environ.Env()
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env_file = str(ROOT_DIR / '.env')
    print(f'Loading : {env_file}')
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# URLS
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# APPS
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#installed-apps
# Default Django apps:
DJANGO_APPS = [
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
# Apps specific for this project:
LOCAL_APPS = [
    'django_q_starter.email_example.apps.EmailExampleConfig',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/3.2/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/3.2/ref/settings/#dirs
        'DIRS': [str(APPS_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # https://docs.djangoproject.com/en/3.2/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # https://docs.djangoproject.com/en/3.2/ref/templates/api/#built-in-template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# Uses django-environ to accept uri format
# See: https://django-environ.readthedocs.io/en/latest/#supported-types
DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#language-code
LANGUAGE_CODE = 'zh-Hant'
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#time-zone
TIME_ZONE = 'Asia/Taipei'
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#use-i18n
USE_I18N = True
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#use-l10n
USE_L10N = True
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/3.2/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / 'locale')]

# STATIC FILE (CSS, JavaScript, Images) CONFIGURATION
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / 'staticfiles')
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#static-url
STATIC_URL = '/static/'
# See: https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / 'static')]
# See: https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / 'uploads')
# See: https://docs.djangoproject.com/en/3.2/ref/settings/#media-url
MEDIA_URL = '/uploads/'

# Sites
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#site-id
SITE_ID = 1

# ADMIN
# ------------------------------------------------------------------------------
ADMIN_URL = 'admin/'

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/3.2/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/3.2/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/3.2/ref/settings/#x-frame-options
X_FRAME_OPTIONS = 'DENY'
