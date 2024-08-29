from celery import Celery

from scrapping.task import log_books
from celery.schedules import crontab

from decouple import config

BROKER_URL = config("BROKER_URL", cast=str)

app = Celery('app', broker=BROKER_URL)

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'celery_app.collect_data',
        'schedule': crontab(hour=7, minute=30),
    },
}
app.conf.timezone = 'UTC'

@app.task
def collect_data():
    print("Collecting data...")
    log_books()
    print("Logs saved.")