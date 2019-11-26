"""
Django settings for bsbackend project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ywh$m7+o$%960v#ivgprv#_klx$gm5pboer^7e0d1^l$kkzcsd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['app-ae25ef7f-eff0-469a-8f73-ef2bbd4b6965.cleverapps.io']
# Development
# '127.0.0.1','localhost',

# Application definition

INSTALLED_APPS = [
    'barriosolidario.apps.BarriosolidarioConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework', # enable rest framework
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bsbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bsbackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

POSTGRESQL_ADDON_URI='postgresql://ug16vxoongcrsk0zfnwt:YAxtbWADgMJb8WaBC33e@baf26ykjxjqujawk8h6k-postgresql.services.clever-cloud.com:5432/baf26ykjxjqujawk8h6k'
POSTGRESQL_ADDON_HOST='baf26ykjxjqujawk8h6k-postgresql.services.clever-cloud.com'
POSTGRESQL_ADDON_DB='baf26ykjxjqujawk8h6k'
POSTGRESQL_ADDON_PASSWORD='YAxtbWADgMJb8WaBC33e'
#APP_HOME='/home/thibault/Documents/barriosolidario/backend/bsbackend/'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR) + '/media'

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR) + '/static'

#STATIC_URL_PREFIX='/static'
#MEDIA_ROOT=APP_HOME+STATIC_URL_PREFIX+'/storage/'
#MEDIA_URL = STATIC_URL_PREFIX+"/storage/"
#STATIC_ROOT = APP_HOME+STATIC_URL_PREFIX+'/static/static/'

POSTGRESQL_ADDON_PORT=5432
POSTGRESQL_ADDON_USER='ug16vxoongcrsk0zfnwt'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', #''django.db.backends.postgresql_psycopg2',  #'django.db.backends.mysql',
        'NAME': POSTGRESQL_ADDON_DB,
        'USER': POSTGRESQL_ADDON_USER,
        'PASSWORD': POSTGRESQL_ADDON_PASSWORD,
        'HOST': POSTGRESQL_ADDON_HOST,
        'PORT': POSTGRESQL_ADDON_PORT,
        'CONN_MAX_AGE': 5,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#Custom User
AUTH_USER_MODEL = 'barriosolidario.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'barriosolidario.customAuthentification.customAuthentification',
)


CORS_ORIGIN_ALLOW_ALL = True
