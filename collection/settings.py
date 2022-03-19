import os
from secrets import token_urlsafe

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = token_urlsafe(16)
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "0.0.0.0",
    "vladtsap.com",
    "collection.vladtsap.com",
]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_bleach",
    "boards",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "collection.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "boards.context_processors.settings_processor"
            ],
        },
    },
]

WSGI_APPLICATION = "collection.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "collection",
        "USER": "postgres",  # redefined in private_settings.py
        "PASSWORD": "postgres",
        "HOST": "postgres",
        "PORT": "5432",
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

LANGUAGE_CODE = "uk-uk"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

DEPLOY = True

TRUE_STATIC = ''
STATIC_URL = "/static/"

# Cache

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}
BOARD_CACHE_SECONDS = 10 * 60  # 10 min

# App settings

APP_NAME = "Краще з найкращого"
APP_TITLE = "Читай інтернет нормально"
APP_DESCRIPTION = APP_TITLE
