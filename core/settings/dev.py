from .base import BASE_DIR

SECRET_KEY = 'django-insecure-i()o2=lv+0fj6f*=ha=rtuxc!g74$kj&t-q9dhh7i*sm6!+0!q'

DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ["https://erp-tunnel.kalodhunga.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}