import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'send_mail.settings')

app = Celery('send_mail')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'spam-5--every-min': {
        'task': 'mainapp.tasks.spam',
        'schedule': crontab(minute='*/3')
    }
}
