from braintree import Configuration, Environment

from .base import *

DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shopsite',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '16.186.79.97',
        'PORT': 5432,
        # 'CONN_MAX_AGE': 5 * 60,
        # 'OPTIONS': {'charset': 'utf8mb4'}
    }
}

ALLOWED_HOSTS = ['*']


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            # 'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

# Braintree settings
BRAINTREE_MERCHANT_ID = '2qf4snfqxsdxqhq4'
BRAINTREE_PUBLIC_KEY = '33bsw4wvhtxk9c8x'
BRAINTREE_PRIVATE_KEY = 'ebd24f1370267d2f46697bf09867fa30'

Configuration.configure(
    Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

# Email Parameters Configurations
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Redis Configurations
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://localhost:6379",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100}
#         }
#     }
# }

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

REDIS_TIMEOUT = 7*24*60*60
CUBES_REDIS_TIMEOUT = 60*60
NEVER_REDIS_TIMEOUT = 365*24*60*60

# CELERY BROKER URL
# CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = 'amqp://localhost'
