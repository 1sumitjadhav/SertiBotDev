"""
Django settings for SertiBotDev project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR=Path(__file__).resolve().parent.parent
LOGIN_REDIRECT_URL=('index/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')$0mnl3ge)dhnrjpx1pk0cp6^wmtfqabhi#+h!+s5=&+t8=@g('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    # 'django.contrib.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'accounts',
=======
<<<<<<< HEAD
    'rest_framework',
    'form',
    'coupons'
=======
    'accounts',
    'Email_handler',
>>>>>>> main
>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SertiBotDev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
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

WSGI_APPLICATION = 'SertiBotDev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

<<<<<<< HEAD

=======
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
<<<<<<< HEAD
=======
<<<<<<< HEAD
        'NAME': 'coupons',
        'USER': 'postgres',
        'PASSWORD': 'mudassir',
        'HOST': '127.0.0.1',
=======
>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'database-1.ceouyqjgp0eq.us-east-1.rds.amazonaws.com',
<<<<<<< HEAD
=======
>>>>>>> main
>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d
        'PORT': '5432',
    }

}

AUTH_USER_MODEL="accounts.User"


AUTH_USER_MODEL="accounts.User"


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR, "static"
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mycareteam.tech'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'billing@mycareteam.tech'
EMAIL_HOST_PASSWORD = 'KY)!zhw_6":3'
EMAIL_USE_SSL = True