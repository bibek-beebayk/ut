import os
from .base import INSTALLED_APPS, MIDDLEWARE

SECRET_KEY = "django-insecure-i()o2=lv+0fj6f*=ha=rcuxc!g74$kj&t-q9dhh7i*sm6!+0!q"

DEBUG = False

ALLOWED_HOSTS = ["ut-production.up.railway.app"]

CSRF_TRUSTED_ORIGINS = ["https://ut-production.up.railway.app"]

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_ACCESS_KEY_ID = "1f8bcff6b47d61799db7beaae02a3fa4"
AWS_SECRET_ACCESS_KEY = (
    "78e32042ccce9896aa5b5767338949146eda472fd532328302be87d2b0ed5260"
)
AWS_STORAGE_BUCKET_NAME = "bonewa"
AWS_S3_ENDPOINT_URL = (
    "https://b46a64eb384beb50a5fc80946bc0abc7.r2.cloudflarestorage.com/bonewa"
)
AWS_S3_SIGNATURE_VERSION = "s3v4"

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

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"