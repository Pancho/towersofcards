import os


here = lambda path: os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '#0by*%_sema)9n+$lp=yok5)l7ovet8g!a3zc7u)#xu-%cz%&y'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'mongoengine.django.mongo_auth',
	'api',
	'realtime',
	'web',
)
MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.tz',
	'django.contrib.messages.context_processors.messages',
	'api.context_processors.static_version',
	'api.context_processors.template_debug',
	'api.context_processors.is_mobile',
	'api.context_processors.realtime_port',
)
ROOT_URLCONF = 'towersofcards.urls'
WSGI_APPLICATION = 'towersofcards.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.dummy'}}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/media/admin/'
APPEND_SLASH = False

try:
	from .localsettings import *
except:
	print('There seems to be an error in your localsettings.py file. Maybe you haven\'t copied it yet from the example.')
