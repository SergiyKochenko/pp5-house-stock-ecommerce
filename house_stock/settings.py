"""
Django settings for house_stock project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import dj_database_url
import boto3  # Added import for boto3

if os.path.exists("env.py"):
    import env

from pathlib import Path

import cloudinary
from botocore.exceptions import ClientError

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if os.environ.get('DEVELOPMENT') == 'True':
    DEBUG = True

ALLOWED_HOSTS = [
    'home-stock-ecommerce-demo-037fe5d891b9.herokuapp.com',
    'localhost',
    '127.0.0.1:8000',
    '*'
]


# Application definition

INSTALLED_APPS = [
    # Jazzmin must be added before 'django.contrib.admin'
    'jazzmin',  # Added Jazzmin for a modern admin interface
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',
    'products',
    'bag',
    'checkout',
    'profiles',
    'newsletter',
    'contactus',
    'about',
    'testimonials',
    'hire',
    'packages',

    # Other apps
    'crispy_forms',
    'crispy_bootstrap4',
    'storages',
    'cloudinary_storage',
    'cloudinary',
]

# Optional Jazzmin Configuration for customizing the admin interface.
JAZZMIN_SETTINGS = { 
    "site_title": "House Stock Admin",
    "site_header": "House Stock Administration",
    "site_brand": "House Stock",
    "site_url": "https://home-stock-ecommerce-demo-037fe5d891b9.herokuapp.com/",
    "welcome_sign": "Welcome to the House Stock Admin Dashboard",
    "search_model": "auth.User",
    "copyright": "House Stock Ltd",
    "show_ui_builder": True,
    "topmenu_links": [
         {"name": "Back to Website", "url": "https://home-stock-ecommerce-demo-037fe5d891b9.herokuapp.com/", "new_window": True},
    ],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-success",
    "navbar": "navbar-cyan navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "solar",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True
}

# IMPORTANT: Place SecurityMiddleware first, followed by WhiteNoise.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'house_stock.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'bag.contexts.bag_contents',
                'testimonials.contexts.get_testimonials',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'house_stock.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'My-Web-Shop',
        "USER": 'agency_l47q_user',
        "PASSWORD": os.environ.get('DB_PASSWORD', ''),
        "HOST": 'dpg-cvfj0s1opnds73batjl0-a.ohio-postgres.render.com',
        "PORT": '5432',
    }
}

# Uncomment below to use sqlite3 in development:
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.sqlite3',
#          'NAME': BASE_DIR / 'db.sqlite3',
#      }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Cloudinary configuration
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
)


if 'USE_AWS' in os.environ:
    # -------------------------------------------------------------------------
    # AWS S3 Configuration for Static and Media Files
    # -------------------------------------------------------------------------
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Configuration with correct region (eu-west-1)
    AWS_STORAGE_BUCKET_NAME = 'pp5-house-stock-ecommerce'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.eu-west-1.amazonaws.com'

    # Custom Storage Settings
    STATICFILES_LOCATION = 'static'
    MEDIAFILES_LOCATION = 'media'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    
    # URLs for static and media files
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

    # Function to check if the S3 bucket is accessible
    def check_bucket_status(bucket_name, region_name):
        """
        Check if the provided S3 bucket is accessible.
        """
        s3_client = boto3.client(
            's3',
            region_name=region_name,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        try:
            s3_client.head_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' is accessible and functioning.")
        except ClientError as error:
            error_code = error.response['Error']['Code']
            if error_code == '403':
                print(f"Bucket '{bucket_name}' exists but access is forbidden (HTTP 403).")
            elif error_code == '404':
                print(f"Bucket '{bucket_name}' does not exist (HTTP 404).")
            else:
                print(f"An error occurred when accessing bucket '{bucket_name}': {error}")

    # Check the Bucket Status
    check_bucket_status(AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)
else:
    # Use Cloudinary for media storage if AWS is not used
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    # Use WhiteNoise for static files in non-AWS environment
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'


# Delivery threshold settings
FREE_DELIVERY_THRESHOLD = 99
STANDARD_DELIVERY_PERCENTAGE = 10


# Stripe settings
STRIPE_CURRENCY = 'usd'
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET', '')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DEFAULT_FROM_EMAIL = 'sergiykochenko@gmail.com'

if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'sergiykochenko@gmail.com.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

# Add the following CSRF trusted origins for Heroku deployments:
CSRF_TRUSTED_ORIGINS = ["https://home-stock-ecommerce-demo-037fe5d891b9.herokuapp.com"]

# Override the default CountrySelectWidget with our custom version:
from profiles.widgets import CustomCountrySelectWidget
import django_countries.widgets
django_countries.widgets.CountrySelectWidget = CustomCountrySelectWidget
