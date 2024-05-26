from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farmDash.settings')

app = Celery('farmDash')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'fetch-data-every-5-seconds': {
        'task': 'main.tasks.fetch_data_from_firebase',
        'schedule': 5.0,  # Every 5 seconds
    },
}
