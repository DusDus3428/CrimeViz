from apscheduler.schedulers.background import BackgroundScheduler
from python_data_gatherer_app import flask_app
from python_data_gatherer_app import la
from python_data_gatherer_app.service import data_portal_service


if __name__ == '__main__':
    # First call needs to be done because scheduler only starts when first interval is reached
    data_portal_service.get_crime_data(la)

    flask_app.logger.info('Starting up background scheduler to request crime data for the city of {} every {} minutes'
                          .format(la.city, la.request_interval))

    scheduler = BackgroundScheduler()
    scheduler.add_job(data_portal_service.get_crime_data, args=[la], trigger='interval', minutes=la.request_interval)
    scheduler.start()

    flask_app.logger.info('Starting up Flask application.')
    flask_app.run()
