from django.core.exceptions import ImproperlyConfigured
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

# SECURITY WARNING: keep the secret key used in production secret!
with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets = secret):
    try:
        return secrets[secret_name]
    except:
        msg="la variable no existe" % secret_name
        raise ImproperlyConfigured(msg)

SECRET_KEY = get_secret("SECRET_KEY")

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Otras apps

)

LOCAL_APPS = (
    'applications.core',
    'applications.services',
    'applications.blog',
    'applications.social',
    'applications.pages',
    'applications.contact',
)

THIRD_PARTY_APPS = (
    'ckeditor',
    # siempre va al ultimo , es para eliminar archivos imagenes. video, etc.
    'django_cleanup.apps.CleanupConfig',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'empresa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                #aca van los processors
                'applications.social.processors.ctx_dict'
            ],
        },
    },
]

WSGI_APPLICATION = 'empresa.wsgi.application'


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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # para que en cada modelo se cree el id auto incremente, esto a partir de django 3.2

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True