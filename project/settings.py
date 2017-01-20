"""
Django settings for sarah_project project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import Config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=phia2=!yholvkg9gqy81(5b(@0p(l&o1ewb0^!76my48swbol'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '127.0.0.1:8080', 'localhost:8080', '*',' 172.20.0.10',]

#DEBUG = False
#ALLOWED_HOSTS = []

#ADMINS = [('Stefan', 'sjsafranek@gmail.com')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'app',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = Config.get_db_config()

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'geo.sqlite3'),
        'OPTIONS': {
			'timeout': 20
        }
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

'''
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'tmp/django_cache',
    }
}
'''

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


# check for lof directory
# create directory if does not exist
if not os.path.exists("log"):
    os.makedirs("log")


LOGGING = {
    
    'version': 1,
    
    'disable_existing_loggers': False,

	'formatters': {
        'color': {
            '()': 'djangocolors_formatter.DjangoColorsFormatter',
			'format': "%(asctime)s [%(levelname)s] [%(name)s] %(filename)s line:%(lineno)d : %(message)s",
        },
        'verbose': {
			'format': "%(asctime)s [%(levelname)s] [%(name)s] %(filename)s line:%(lineno)d : %(message)s",
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'handlers': {
        'server': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/server.log',
            'formatter': 'verbose'
        },
        'django': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/django.log',
            'formatter': 'verbose'
        },
        'worker': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/worker.log',
            'formatter': 'verbose'
        },
        'api': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/api.log',
            'formatter': 'verbose'
        },
		'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console','django'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
			'handlers': ['console','django'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.server': {
			'handlers': ['console','django'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.template': {
			'handlers': ['console','django'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
			'handlers': ['console','django'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security.*': {
            'handlers': ['console','django'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'worker': {
            'handlers': ['console','worker'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'api': {
            'handlers': ['console','api'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    
}
