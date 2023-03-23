from pathlib import WindowsPath

### ABSOLUTE_URL_OVERRIDES = {}
### ADMINS = []
### ALLOWED_HOSTS = []
### APPEND_SLASH = True
### AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]
### AUTH_USER_MODEL = 'auth.User'
BASE_DIR = WindowsPath("E:/VS_Code/Django_Codemy/Django_Codemy")  ###
### CACHES = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
### CACHE_MIDDLEWARE_ALIAS = 'default'
### CACHE_MIDDLEWARE_KEY_PREFIX = ''
### CACHE_MIDDLEWARE_SECONDS = 600
### CSRF_COOKIE_AGE = 31449600
### CSRF_COOKIE_DOMAIN = None
### CSRF_COOKIE_HTTPONLY = False
### CSRF_COOKIE_MASKED = False
### CSRF_COOKIE_NAME = 'csrftoken'
### CSRF_COOKIE_PATH = '/'
### CSRF_COOKIE_SAMESITE = 'Lax'
### CSRF_COOKIE_SECURE = False
### CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
### CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
### CSRF_TRUSTED_ORIGINS = []
### CSRF_USE_SESSIONS = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": WindowsPath(
            "E:/VS_Code/Django_Codemy/Django_Codemy/db.sqlite3"
        ),
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "CONN_HEALTH_CHECKS": False,
        "OPTIONS": {},
        "TIME_ZONE": None,
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "TEST": {
            "CHARSET": None,
            "COLLATION": None,
            "MIGRATE": True,
            "MIRROR": None,
            "NAME": None,
        },
    }
}
### DATABASE_ROUTERS = []
### DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440
### DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000
### DATA_UPLOAD_MAX_NUMBER_FILES = 100
### DATETIME_FORMAT = 'N j, Y, P'
### DATETIME_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f',
# '%Y-%m-%d %H:%M', '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M:%S.%f', '%m/%d/%Y %H:%M',
# '%m/%d/%y %H:%M:%S', '%m/%d/%y %H:%M:%S.%f', '%m/%d/%y %H:%M']
### DATE_FORMAT = 'N j, Y'
### DATE_INPUT_FORMATS = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
# '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y']
DEBUG = True
### DEBUG_PROPAGATE_EXCEPTIONS = False
### DECIMAL_SEPARATOR = '.'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
### DEFAULT_CHARSET = 'utf-8'
### DEFAULT_EXCEPTION_REPORTER = 'django.views.debug.ExceptionReporter'
### DEFAULT_EXCEPTION_REPORTER_FILTER = 'django.views.debug.SafeExceptionReporterFilter'
### DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
### DEFAULT_FROM_EMAIL = 'webmaster@localhost'
### DEFAULT_INDEX_TABLESPACE = ''
### DEFAULT_TABLESPACE = ''
### DISALLOWED_USER_AGENTS = []
### EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
### EMAIL_HOST = 'localhost'
### EMAIL_HOST_PASSWORD = ''
### EMAIL_HOST_USER = ''
### EMAIL_PORT = 25
### EMAIL_SSL_CERTFILE = None
### EMAIL_SSL_KEYFILE = None
### EMAIL_SUBJECT_PREFIX = '[Django] '
### EMAIL_TIMEOUT = None
### EMAIL_USE_LOCALTIME = False
### EMAIL_USE_SSL = False
### EMAIL_USE_TLS = False
### FILE_UPLOAD_DIRECTORY_PERMISSIONS = None
### FILE_UPLOAD_HANDLERS = ['django.core.files.uploadhandler.MemoryFileUploadHandler',
# 'django.core.files.uploadhandler.TemporaryFileUploadHandler']
### FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440
### FILE_UPLOAD_PERMISSIONS = 420
### FILE_UPLOAD_TEMP_DIR = None
### FIRST_DAY_OF_WEEK = 0
### FIXTURE_DIRS = []
### FORCE_SCRIPT_NAME = None
### FORMAT_MODULE_PATH = None
### FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'
### IGNORABLE_404_URLS = []
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "learn.apps.LearnConfig",
]
### INTERNAL_IPS = []
### LANGUAGES = [('af', 'Afrikaans'), ('ar', 'Arabic'), ('ar-dz', 'Algerian Arabic'),
# ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'),
# ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'),
# ('ca', 'Catalan'), ('ckb', 'Central Kurdish (Sorani)'), ('cs', 'Czech'),
# ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'),
# ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'),
# ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'),
# ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'),
# ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'),
# ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'),
# ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'),
# ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'),
# ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'),
# ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ig', 'Igbo'),
# ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'),
# ('ka', 'Georgian'), ('kab', 'Kabyle'), ('kk', 'Kazakh'), ('km', 'Khmer'),
# ('kn', 'Kannada'), ('ko', 'Korean'), ('ky', 'Kyrgyz'), ('lb', 'Luxembourgish'),
# ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'),
# ('mn', 'Mongolian'), ('mr', 'Marathi'), ('ms', 'Malay'), ('my', 'Burmese'),
# ('nb', 'Norwegian Bokmσl'), ('ne', 'Nepali'), ('nl', 'Dutch'),
# ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'),
# ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'),
# ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'),
# ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'),
# ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'),
# ('th', 'Thai'), ('tk', 'Turkmen'), ('tr', 'Turkish'), ('tt', 'Tatar'),
# ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'),
# ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'),
# ('zh-hant', 'Traditional Chinese')]
### LANGUAGES_BIDI = ['he', 'ar', 'ar-dz', 'ckb', 'fa', 'ur']
LANGUAGE_CODE = "en-in"
### LANGUAGE_COOKIE_AGE = None
### LANGUAGE_COOKIE_DOMAIN = None
### LANGUAGE_COOKIE_HTTPONLY = False
### LANGUAGE_COOKIE_NAME = 'django_language'
### LANGUAGE_COOKIE_PATH = '/'
### LANGUAGE_COOKIE_SAMESITE = None
### LANGUAGE_COOKIE_SECURE = False
### LOCALE_PATHS = []
### LOGGING = {}
### LOGGING_CONFIG = 'logging.config.dictConfig'
### LOGIN_REDIRECT_URL = '/accounts/profile/'
### LOGIN_URL = '/accounts/login/'
### LOGOUT_REDIRECT_URL = None
### MANAGERS = []
### MEDIA_ROOT = ''
### MEDIA_URL = ''
### MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
### MIGRATION_MODULES = {}
### MONTH_DAY_FORMAT = 'F j'
### NUMBER_GROUPING = 0
### PASSWORD_HASHERS = ['django.contrib.auth.hashers.PBKDF2PasswordHasher',
# 'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
# 'django.contrib.auth.hashers.Argon2PasswordHasher',
# 'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
# 'django.contrib.auth.hashers.ScryptPasswordHasher']
### PASSWORD_RESET_TIMEOUT = 259200
### PREPEND_WWW = False
ROOT_URLCONF = "Code.urls"  ###
SECRET_KEY = """aHbRz5mJNTn6Rmm7IXSLbOk75CUWSKwLXavE2xX4aiPPpWwwpaVEhO4jTxuNcDLwAkUo
FZO4A7Z0KBepxfP7D6QHeicsh6nash4FzQgreQgYtt7o2fpCM1SL7eSohPy8pikZbnqDLu4q4f07BWbQXdJy
pRn71A0az0WC1KNVTYt1Lt063cvRVpxiA1rfSKC7clOzkJr6ONMJ0Hm84EZwyKeDU9zq8qRFYwDjQbpWcBfw
TaTyRkoLvbM9HyTEHaVp"""
### SECRET_KEY_FALLBACKS = []
### SECURE_CONTENT_TYPE_NOSNIFF = True
### SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'
### SECURE_HSTS_INCLUDE_SUBDOMAINS = False
### SECURE_HSTS_PRELOAD = False
### SECURE_HSTS_SECONDS = 0
### SECURE_PROXY_SSL_HEADER = None
### SECURE_REDIRECT_EXEMPT = []
### SECURE_REFERRER_POLICY = 'same-origin'
### SECURE_SSL_HOST = None
### SECURE_SSL_REDIRECT = False
### SERVER_EMAIL = 'root@localhost'
### SESSION_CACHE_ALIAS = 'default'
### SESSION_COOKIE_AGE = 1209600
### SESSION_COOKIE_DOMAIN = None
### SESSION_COOKIE_HTTPONLY = True
### SESSION_COOKIE_NAME = 'sessionid'
### SESSION_COOKIE_PATH = '/'
### SESSION_COOKIE_SAMESITE = 'Lax'
### SESSION_COOKIE_SECURE = False
### SESSION_ENGINE = 'django.contrib.sessions.backends.db'
### SESSION_EXPIRE_AT_BROWSER_CLOSE = False
### SESSION_FILE_PATH = None
### SESSION_SAVE_EVERY_REQUEST = False
### SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SETTINGS_MODULE = "Code.settings"  ###
### SHORT_DATETIME_FORMAT = 'm/d/Y P'
### SHORT_DATE_FORMAT = 'm/d/Y'
### SIGNING_BACKEND = 'django.core.signing.TimestampSigner'
### SILENCED_SYSTEM_CHECKS = []
### STATICFILES_DIRS = []
### STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.FileSystemFinder',
# 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
### STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
### STATIC_ROOT = None
STATIC_URL = "static/"
### STORAGES = {'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
# 'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'}}
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
            ]
        },
    }
]
### TEST_NON_SERIALIZED_APPS = []
### TEST_RUNNER = 'django.test.runner.DiscoverRunner'
### THOUSAND_SEPARATOR = ','
### TIME_FORMAT = 'P'
### TIME_INPUT_FORMATS = ['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']
TIME_ZONE = "Asia/Calcutta"
### USE_DEPRECATED_PYTZ = False
### USE_I18N = True
### USE_L10N = True
### USE_THOUSAND_SEPARATOR = False
USE_TZ = True
### USE_X_FORWARDED_HOST = False
### USE_X_FORWARDED_PORT = False
WSGI_APPLICATION = "Code.wsgi.application"
### X_FRAME_OPTIONS = 'DENY'
### YEAR_MONTH_FORMAT = 'F Y'
