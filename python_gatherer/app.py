from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from service import data_portal_service
from service import la

app = Flask(__name__)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(data_portal_service.get_crime_data(la), 'interval', minutes=la.request_interval)
    scheduler.start()