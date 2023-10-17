import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Poketasks.settings')

app = Celery('Poketasks')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
