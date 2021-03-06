"""
Django settings for lykops project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1tz5l71&-u4u0j^+hf02h90&xqjlqse*!5tn0fr=4-skao7f5k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_crontab',
    'bootstrap_toolkit',
    
    'basicdata',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    'django.middleware.common.CommonMiddleware' ,
    'django.contrib.sessions.middleware.SessionMiddleware' ,
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'lykops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates/"),
            os.path.join(BASE_DIR, "basicdata/templates/"),
            os.path.join(BASE_DIR, "lykops/templates/"),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                ],
        },
    },
]


WSGI_APPLICATION = 'lykops.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'lykops',
        'USER' : 'lykops',
        'PASSWORD' :'!QAZxdr5^YHN',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'OPTIONS': {  
            'charset': 'utf8',
            'use_unicode': True,
        },
    },
             
    'mysql_write': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'lykops',
        'USER' : 'lykops',
        'PASSWORD' :'!QAZxdr5^YHN',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'OPTIONS': {  
              'charset': 'utf8',  
              'use_unicode': True,  
        },  
    } ,

    'mysql_read': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'lykops',
        'USER' : 'lykops',
        'PASSWORD' :'!QAZxdr5^YHN',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'OPTIONS': {  
              'charset': 'utf8',  
              'use_unicode': True,  
        },  
    },
}


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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
#'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

MEDIA_URL = '/file/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'file')


STATIC_URL = '/static/'  # 若存放静态文件的static目录在app目录下，则改局生效，无需定义下面的

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 若存放静态文件的static目录在project目录下，则用该定义

'''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    )

BOOTSTRAP_BASE_URL = os.path.join(STATIC_ROOT, 'bootstrap')
BOOTSTRAP_CSS_BASE_URL = os.path.join(BOOTSTRAP_BASE_URL, 'css')
# BOOTSTRAP_CSS_URL       = BOOTSTRAP_CSS_BASE_URL + 'bootstrap.css'
BOOTSTRAP_JS_BASE_URL = os.path.join(BOOTSTRAP_BASE_URL, 'js')
# Enable for single bootstrap.js file
# BOOTSTRAP_JS_URL        = BOOTSTRAP_JS_BASE_URL + 'bootstrap.js'
STATICFILES_DIRS = (
    ('b_css', BOOTSTRAP_CSS_BASE_URL),
    ('b_js', BOOTSTRAP_JS_BASE_URL),
    STATIC_URL,
)
'''
