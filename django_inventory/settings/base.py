"""
Django settings for Django Inventory project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from pathlib import Path

# import django
# django.setup()


#BASE_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4#8p2r=zfa=t@3@@v5v*)i=kvnuyxae_yyvqkyv4!opcwad6@+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',

    'constance',
    'constance.backends.database',

    # 3rd party
    #$# 010
    #'south',
    'photologue',
    # Project
    'photos',
    'common',
    'generic_views',
    'inventory',
    'assets',
    'dynamic_search',
    #'importer',
    'movements',
    'main',
    'web_theme',
)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


ROOT_URLCONF = 'django_inventory.urls'

WSGI_APPLICATION = 'django_inventory.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Custom settings section

from django.urls import reverse_lazy

PROJECT_TITLE = 'Django Inventory'
PROJECT_NAME = 'django_inventory'

ugettext = lambda s: s

LANGUAGES = (
    ('es', ugettext('Spanish')),
    ('en', ugettext('English')),
    ('ru', ugettext('Russian')),
)

SITE_ID = 1

STATIC_URL = '/static/'

#sys.path.append(os.path.join(BASE_DIR, 'django_inventory', 'apps'))

MEDIA_ROOT = os.path.join(BASE_DIR, 'django_inventory', 'media')
STATIC_ROOT = os.path.join(MEDIA_ROOT, 'static')

MEDIA_URL = '/site_media/'

LOGIN_URL = reverse_lazy('login_view')
LOGIN_REDIRECT_URL = reverse_lazy('home')

# --------- Django compressor -------------
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_ENABLED = False

# -------- LoginRequiredMiddleware ----------
LOGIN_EXEMPT_URLS = (
    r'^favicon\.ico$',
    r'^about\.html$',
    r'^legal/',  # allow the entire /legal/* subsection
    r'^static/',

    r'^accounts/register/$',
    r'^accounts/register/complete/$',
    r'^accounts/register/closed/$',

    r'^accounts/activate/complete/',
    r'^accounts/activate/(?P<activation_key>\w+)/$',

    r'^password/reset/$',
    r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
    r'^password/reset/complete/$',
    r'^password/reset/done/$',
)

# --------- Generic photos --------------
# PHOTOS_MAX_PHOTO_SIZE = 1000000
# INVENTORY_MAX_TEMPLATE_PHOTOS = 5
# ASSETS_MAX_ASSET_PHOTOS = 5
# ASSETS_MAX_PERSON_PHOTOS = 5
# --------- Pagination ------------------

PAGINATION_DEFAULT_PAGINATION = 10

# --------- Web theme app ---------------
WEB_THEME = 'warehouse'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'