from datetime import timedelta
from os import getenv
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = SRC_DIR.parent

SECRET_KEY = getenv("DJANGO_SECRET_KEY", default="INVALID")
DEBUG = getenv("DJANGO_DEBUG", default=False)
ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", default="").split(",")

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
]

LOCAL_APPS = [
    "exchange_rates",
    "users",
    "tickets",
    "comments",
    "core",
    "shared",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": ROOT_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("PSQL_NAME"),
        "USER": getenv("PSQL_USER"),
        "PASSWORD": getenv("PSQL_PASSWORD"),
        "HOST": getenv("PSQL_HOST"),
        "PORT": getenv("PSQL_PORT"),
    }
}

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Set custom user model
AUTH_USER_MODEL = "users.User"

# Exchange rates service (Alpha Vantage)
ALPHA_VANTAGE_BASE_URL = getenv(
    "ALPHA_VANTAGE_BASE_URL",
    default="https://www.alphavantage.co",
)
ALPHA_VANTAGE_API_KEY = getenv("ALPHA_VANTAGE_API_KEY")


# DRF configuration
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}
