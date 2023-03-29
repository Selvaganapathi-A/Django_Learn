"""
Django settings for Code project.

Generated by 'django-admin startproject' using Django 4.2b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from pathlib import Path

APPEND_SLASH = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # type: ignore


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "aHbRz5mJNTn6Rmm7IXSLbOk75CUWSKwLXavE2xX4aiPPpWwwpaVEh"
    + "O4jTxuNcDLwAkUoFZO4A7Z0KBepxfP7D6QHeicsh6nash4FzQgre"
    + "QgYtt7o2fpCM1SL7eSohPy8pikZbnqDLu4q4f07BWbQXdJypRn71"
    + "A0az0WC1KNVTYt1Lt063cvRVpxiA1rfSKC7clOzkJr6ONMJ0Hm84"
    + "EZwyKeDU9zq8qRFYwDjQbpWcBfwTaTyRko"
    + "LvbM9HyTEHaVp"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "*",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Created Apps
    "learn.apps.LearnConfig",
    "members.apps.MembersConfig",
    "vulture.apps.VultureConfig"
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

ROOT_URLCONF = "Code.urls"

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

ASGI_APPLICATION = "Code.asgi.application"

WSGI_APPLICATION = "Code.wsgi.application"

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "CONN_HEALTH_CHECKS": False,
        "OPTIONS": {},
        "TIME_ZONE": None,
        "USER": "postgres",
        "PASSWORD": "Windows@11",
        "HOST": "localhost",
        "PORT": "5432",
        "TEST": {
            "CHARSET": None,
            "COLLATION": None,
            "MIGRATE": True,
            "MIRROR": None,
            "NAME": None,
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth."
        + "password_validation.UserAttributeSimilarityValidator",
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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = "en-in"

TIME_ZONE = "Asia/Calcutta"

USE_I18N = True

USE_TZ = True


# Media files (User Uploaded files Like, Images, Videos, Documents)
MEDIA_ROOT = BASE_DIR / "_Media"
MEDIA_URL = "media/" if DEBUG else "http://localhost:4000/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "_Static",
]
STATIC_ROOT = BASE_DIR / "Static"
STATIC_URL = "static/" if DEBUG else "http://localhost:3000/"

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
