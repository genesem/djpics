
STATIC_ROOT = '../www/static/'
MEDIA_ROOT = '../www/media/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Settings:
# https://docs.djangoproject.com/en/2.0/topics/settings/
# https://docs.djangoproject.com/en/2.0/ref/settings/
# Static files:
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
# i18n:
# https://docs.djangoproject.com/en/2.0/topics/i18n/

from os import path

# путь к локальной базе только для примера
# BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
dbpath = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'db.sqlite3')

SECRET_KEY = '(9us#tadfg2f4=g8sxybblc0l7r3t)'

DEBUG = True # не для production!
ALLOWED_HOSTS = []
ROOT_URLCONF = 'main.urls'
WSGI_APPLICATION = 'main.wsgi.app'

INSTALLED_APPS = [
    'main',                    # <- 'main' module
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.staticfiles', # не исп.
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',  # заголовок формируется nginx т.е. тут не нужен
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templ'],
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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': dbpath # path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
