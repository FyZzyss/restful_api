import os

from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testwork.settings')
 
celery_app = Celery('testwork')
celery_app.config_from_object('django.conf:settings',namespace='CELERY')
 
# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()

@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))