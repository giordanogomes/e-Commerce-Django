"""
Configurações do Django para o projeto pystore.

Gerado por 'django-admin startproject' usando Django 4.0.2.

Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/4.0/topics/settings/

Para obter a lista completa de configurações e seus valores, consulte
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Construa caminhos dentro do projeto assim: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações de desenvolvimento de início rápido - inadequadas para produção
# Veja https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# AVISO DE SEGURANÇA: mantenha a chave secreta usada na produção em segredo!
SECRET_KEY = 'django-insecure-&=jl)1+=t705&=v#!yu^@r@m$@1ampm7h9((i!2o1j6-s9yk^c'

# AVISO DE SEGURANÇA: não execute com o debug ativado em produção!
DEBUG = True

ALLOWED_HOSTS = []


# Definição do aplicativo

INSTALLED_APPS = [
    # djando apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps de terceiros
    'debug_toolbar',
    'widget_tweaks',
    # meus apps
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'products.apps.ProductsConfig',
    'cart.apps.CartConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'pystore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'pystore.wsgi.application'


# Base de dados
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validação de senha
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internacionalização
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Belem'

USE_I18N = True

USE_TZ = True


# Arquivos estáticos (CSS, JavaScript, Imagens)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"


# Modelo de Usuário
AUTH_USER_MODEL = "users.User"

# Tipo de campo de chave primária padrão
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Mídias
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# django-debug
import socket

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]

# cart

CART_SESSION_ID = "cart"
CART_ITEM_MAX_QUANTITY = 20
