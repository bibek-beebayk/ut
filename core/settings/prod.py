import os

SECRET_KEY = "django-insecure-i()o2=lv+0fj6f*=ha=rcuxc!g74$kj&t-q9dhh7i*sm6!+0!q"

DEBUG = False

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ["https://erp-tunnel.kalodhunga.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("PGDATABASE", "ut"),
        "USER": os.environ.get("PGUSER", "postgres"),
        "PASSWORD": os.environ.get("PGPASSWORD", ""),
        "HOST": os.environ.get("PGHOST", ""),
        "PORT": os.environ.get("PGPORT", ""),
        "ATOMIC_REQUESTS": True,
    }
}
