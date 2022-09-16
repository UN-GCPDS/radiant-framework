"""
Django settings for dimawebapp project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import sys
import django.views.debug
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&-%3g&h#^q8%fnsxg27jwe*^u+az&&zcp$_!rh%w&1ekh#_2!n"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False) == 'True'
PROTECT = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '172.23.177.246']

if DEBUG:
    def wing_debug_hook(*args, **kwargs):
        if __debug__ and 'WINGDB_ACTIVE' in os.environ:
            exc_type, exc_value, traceback = sys.exc_info()
            sys.excepthook(exc_type, exc_value, traceback)
        return old_technical_500_response(*args, **kwargs)

    old_technical_500_response = django.views.debug.technical_500_response
    django.views.debug.technical_500_response = wing_debug_hook


# Application definition

INSTALLED_APPS = [

    'admin_interface',
    'colorfield',

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'django_extensions',
    # 'rest_framework',

    # 'django_plotly_dash.apps.DjangoPlotlyDashConfig',

    # 'research_groups.apps.ResearchGroupsConfig',

    'visualizations.apps.VisualizationsConfig',

    'researchers.apps.ResearchersConfig',
    'groups.apps.GroupsConfig',
    'dima.apps.DimaConfig',
    'projects.apps.ProjectsConfig',
    'bulk_data.apps.BulkDataConfig',
    'unal_plantilla_web.apps.UnalPlantillaWebConfig',
    'intellectual_property.apps.IntellectualPropertyConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if PROTECT:
    MIDDLEWARE.append('csp.middleware.CSPMiddleware')

ROOT_URLCONF = "dimawebapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = "dimawebapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

db_file = os.path.join(BASE_DIR, "db.sqlite3")
if DEBUG or os.path.exists(db_file):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": db_file,
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mysite',
            'USER': 'mysite',
            'PASSWORD': 'electronica',
            'HOST': '/tmp/mysql.sock',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'resources')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


#
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

if PROTECT:

    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CROSS_ORIGIN_OPENER_POLICY = 'SAMEORIGIN'
    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = 'SAMEORIGIN'
    APPEND_SLASH = True

    CSRF_COOKIE_HTTPONLY = True
    CSRF_USE_SESSIONS = True
    CSRF_COOKIE_SAMESITE = 'Strict'

    SESSION_COOKIE_SAMESITE = 'Strict'
    SESSION_COOKIE_HTTPONLY = True

    STYLE_HASHES = [
        'sha256-47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=',
        'sha256-aiTj2pLXNZHW9Z9KTiqS/nAlzlmLv82TyKGz+I/RMeE=',
        'sha256-iH23oQFQFzAwzg6myWBu40yKvLxWiaNJtPaJUQmn1R8=',
        'sha256-aqNNdDLnnrDOnTNdkJpYlAxKVJtLt9CtFLklmInuUAE=',
        'sha256-aV3p0L0H4ndj7jdNR4+mI4+7d697pGiRmrTzmBsGxzI=',
        'sha256-6hLz0852u+x0xB22EdtSAOB0auGKeD1w7gJUvgIJ4I0=',
        'sha256-cUFuwp4e078DeooEUfiR1pq5f2G7IrZQoHa/JYi5B+4=',
        'sha256-vCpS8VyHtSqXbN/JkDhke+jauUq+p7lBAVCL+C75wZo=',
        'sha256-ZqhM5xQOj0Og/l+8qEbc5F5YYumTdWvc5mtn7dECFuE=',
    ]

    SCRIPT_HASHES = [
        'sha256-qdaIOdxVXcIztjBR66IohY2PwX8bhu2A4QaVkQmqlHo=',
        'sha256-PX4TD8hriRso3HL8sYY68HAq+dAa2fOjejIlZcsCyEM=',
        'sha256-jqZuiIXV/j//M8wzFf3TcM9ILcc1us445Jk/TgGEHPA=',
        'sha256-YjTxNZcoFhMDTI70uRNH1V6gP6qpJNGnAlWVb7gVcHM=',
        'sha256-8maZJNlpOzTu6EL0u4JmdqQTIAdNJ6ySEtH2WAbiWb8=',
    ]

    SCRIPT_EXTERN = [
        'http://www.google.com/',
        'http://cse.google.com/',
    ]

    CSP_STYLE_SRC = ["'self'"] + SCRIPT_EXTERN + [f"'{hash_}'" for hash_ in STYLE_HASHES]
    CSP_SCRIPT_SRC = ["'self'", "'unsafe-eval'"] + SCRIPT_EXTERN + [f"'{hash_}'" for hash_ in SCRIPT_HASHES]
    CSP_INCLUDE_NONCE_IN = ['script-src', 'style-src']
    CSP_FRAME_ANCESTORS = ["'none'"]
    CSP_FORM_ACTION = ["'self'"]
    CSP_IMG_SRC = ["'self'", "data:"]
    CSP_FONT_SRC = ["'self'"]
    CSP_CONNECT_SRC = ["'self'"]
    CSP_OBJECT_SRC = ["'none'"]
    CSP_BASE_URI = ["'none'"]
    CSP_DEFAULT_SRC = ["'none'"]
