from celery import Celery

from scrapping.task import log_books

from celery.schedules import crontab

from decouple import config

BROKER_URL = config("BROKER_URL", cast=str)


celery_app = Celery('setup', broker=BROKER_URL)

celery_app.conf.timezone = 'America/Sao_Paulo'
celery_app.conf.broker_connection_retry_on_startup = True

celery_app.conf.beat_schedule = {
    'Get Book Data': {
        'task': 'setup.celery.collect_data',
        'schedule': crontab(hour="14", minute="20"),
    },
}

celery_app.conf.timezone = 'UTC'

@celery_app.task
def collect_data():
    print("Collecting data...")
    log_books()
    print("Logs saved.")