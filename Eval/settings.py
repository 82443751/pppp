# -*- coding: UTF-8 -*-

"""
Django settings for Eval project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g1^f$9*624x9=px22_be053_!2w7=97o6538et2ppe%-vw4(*^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'backend',
    'app',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# MIGRATION_MODULES = {'backend': 'backend.db_migrations'}
ROOT_URLCONF = 'Eval.urls'

WSGI_APPLICATION = 'Eval.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'eval',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'onbsd12',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }

}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
LANGUAGES = (
    ('zh', u'中文'),
    ('en', 'English'),
)
LANGUAGE_COOKIE_NAME = 'django_language'
TIME_ZONE = 'Asia/Shanghai'
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'
USE_I18N = True

USE_L10N = True

USE_TZ = True
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_ROOT = r'E:\works\eval\media'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# STATIC_ROOT = '/Users/echo/Documents/works/nworkspace/Eval/static'
# STATIC_ROOT = r'E:\works\eval\static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader')
LOCALE_PATHS = (os.path.join(BASE_DIR,'locale'),)

CURRENT_LANG_CODE = LANGUAGE_CODE

LOGGING_PAYMENT = os.path.join(BASE_DIR,'pay.log')

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
}
# CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_JQUERY_URL = 'http://cdn.bootcss.com/jquery/2.1.1/jquery.min.js'

EMAIL_SUBJECT_PREFIX = u'[爱在人间]'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'eval@aizairenjian.com'
EMAIL_HOST_PASSWORD = 'Buzhudaogao1234567'

EMAIL_HOST = 'smtp.mxhichina.com'
EMAIL_USE_SSL = False
ZH_LANG_CODE = 'zh'
EN_LANG_CODE = 'en'
