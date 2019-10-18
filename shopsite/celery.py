import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
profile = os.environ.get('PROJECT_PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopsite.settings.%s' % profile)

app = Celery('shopsite')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
