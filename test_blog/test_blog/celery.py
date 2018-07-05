import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_blog.settings')

app = Celery('test_blog')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
