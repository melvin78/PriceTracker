from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jumia.settings')

app = Celery('jumia')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'UTC'
# Load task modules from all registered Django app configs.
app.conf.beat_schedule = {

    "every two hours": {
        "task": "compare_phoneplace",
        'schedule': crontab(hour='*/2'),
    }
}

app.autodiscover_tasks()

#
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))


