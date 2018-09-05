from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deployment.settings')

if os.environ.get('IS_PRODUCTION', None):
    url = "redis://redis:6379"
else:
    url = "redis://localhost:6379"

app = Celery('deployment', broker=url, backend=url)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
