"""
Django settings for sarah_project project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=phia2=!yholvkg9gqy81(5b(@0p(l&o1ewb0^!76my48swbol'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
	'formatters': {
        'color': {
            #'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            '()': 'djangocolors_formatter.DjangoColorsFormatter',
			'format': "%(asctime)s [%(levelname)s] [%(name)s] %(filename)s line:%(lineno)d : %(message)s",
        },
        'verbose': {
            #'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
			'format': "%(asctime)s [%(levelname)s] [%(name)s] %(filename)s line:%(lineno)d : %(message)s",
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'log/server.log',
            'formatter': 'verbose'
        },
		'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console','file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
			'handlers': ['console','file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.server': {
			'handlers': ['console','file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.template': {
			'handlers': ['console','file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
			'handlers': ['console','file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.security.*': {
			'handlers': ['console','file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
