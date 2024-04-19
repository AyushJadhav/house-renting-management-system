"""
Django settings for house_renting_management_system project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7_&n=e4j3sle=gi1#m8bh#v8^pnq!7*g)e$r9ud7(5%_r-8wn2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['c6ac8cebb11844a1b76e3ea6d970f2de.vfs.cloud9.eu-west-1.amazonaws.com',
'house-renting-system-x23178248-env-1.eba-4y7b5hzt.eu-west-2.elasticbeanstalk.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'rest_framework',
    'properties',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

CSRF_TRUSTED_ORIGINS = [
    'https://c6ac8cebb11844a1b76e3ea6d970f2de.vfs.cloud9.eu-west-1.amazonaws.com',  
]





ROOT_URLCONF = 'house_renting_management_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'house_renting_management_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'jadhavayush2020@gmail.com'
EMAIL_HOST_PASSWORD= 'jlei wcfc ebxm mlao'

AWS_ACCESS_KEY_ID = 'ASIATUYJP7SUDYQDTMIU'
AWS_SECRET_ACCESS_KEY = 'rRbJEWbkTHcknpweeH563Hv3hXcumQ1kYKjtKahc'
AWS_SESSION_TOKEN='IQoJb3JpZ2luX2VjELX//////////wEaCXVzLWVhc3QtMSJHMEUCIQC+Pdry8bgjYU1NZbcFdMXBA9AWjTnzHjz7/whW9Ifo8gIgfiKwv7cEWYrdzaTylmMhDX7sOshmP7eydZlxCUeOqYwqiAQI7f//////////ARADGgwyNTA3Mzg2Mzc5OTIiDMNl8JMzFqBqJ5oEbSrcA2TGD3GARHvnUfH4MOJMkmCSqBlziEzEoqbxz4xrC2VNZ0u5Z7jO93Tq0FVgWW176KEFs6Xwj3rLROYTgjFTqreCOSbZIXWH57bDDKkcE5m6slXHd4nlxxoNWHPmTevprjiiuYaho3zh1rjZoarvoWXm+yeWkKq2evP5TVttMIZTtMemd33ioEe9ybPE/ZjD//hXtMGY4GRAZP/WO/7wvBKfHBfT2kNLuqOGwKdIputZuwhfeuvSJMwnYotSGlW4ElnbTFgeTVK8XUNjY3b0zuXgvPM3hIf0n9hIgvwbFkydYJpjInXTK1v3i/T4w7wHScA1KqJaPb8uI9BQCHzSFMzvgkLQ02lzGIV+TvLHDRVqaJx4QZLvcGcqUuFCdV2mJ2DW4kPYEcuUtiQGi8VkokwG0sVk8/RNnIPLbX9hpaUGTGsaYtUiStkxr6oNoJVHxDftQHJkhXuUV+QYG4o9SYMgB6EeumEO3E3abvWX1vt44RhHo1v/3QdZGhJDPIYwLVy56DeglcE0w0gDSUP5v64sCWKtaAS2gLQwsZOI6uhIt5KNuWSTZn6Fa/QVP2DGyPIO8MzdQ14FmrIQbtJRwFAHu313SdrY8wwhvUZHmqECu/8phPgpmB0vhpZxMPeahLEGOqYBZQJqvSc/wq3AIFlbcGBY6XhmBez5f9mqVgHqW4KziD1iSilrp/TpPGRiv9YKAz6c8l5Sx1kLLOJJfhEKWP8rlMhXRSKClfu7Rf3MdmjGP/pMPddK2lOJWakosu26kCQZ7xW8d4f9QZ7tX3dDs9NDr4nq6nI+/K+0RlnmCualViOV+/7avHjHMQTz22FaJ3YDEmAQfNSXBW4XeGwMKjfZNTPRzsp9SA=='
AWS_STORAGE_BUCKET_NAME = 'x23178248-cpp'
AWS_S3_REGION_NAME = 'eu-west-1'  # e.g., us-east-1
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# For serving static files directly from S3
AWS_S3_URL_PROTOCOL = 'https'
AWS_S3_USE_SSL = True
AWS_S3_VERIFY = True

# Static and media file configuration
STATIC_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_MEDIA_BUCKET_PREFIX = 'media/house_images/'

