from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from wa_notification import alertApi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(alertApi.medicine_time_alert, 'interval', minutes=1)
    scheduler.start()