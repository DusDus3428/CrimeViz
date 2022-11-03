import requests
from python_gatherer_app import flask_app


def get_crime_data(target_data_portal):
    flask_app.logger.info('Sending request for crime data to portal {} with the endpoint {}'
                          .format(target_data_portal.data_portal, target_data_portal.api_endpoint))

    custom_headers = {'X-App-Token': target_data_portal.app_token}
    response = requests.get(target_data_portal.api_endpoint, headers=custom_headers)

    match response.status_code:
        case 200:
            flask_app.logger.info('{} - Crime data received.'.format(response.status_code))
        case 400:
            flask_app.logger.error('{} - Bad request.'.format(response.status_code))
        case 401:
            flask_app.logger.error('{} - Unauthorized. Check Socrata docs on how to authenticate properly'
                                   .format(response.status_code))
        case 403:
            flask_app.logger.error('{} - Forbidden. You need to authenticate the application.'
                                   .format(response.status_code))
        case 404:
            flask_app.logger.error('{} - Not found. Resource does not exist.'.format(response.status_code))
        case 429:
            flask_app.logger.error('{} - Request denied because your application has been throttled.'
                                   .format(response.status_code))
        case 500:
            flask_app.logger.info('{} - Internal server error. Check Socrata for more info.'
                                  .format(response.status_code))
