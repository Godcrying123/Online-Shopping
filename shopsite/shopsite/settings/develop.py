from braintree import Configuration, Environment

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1