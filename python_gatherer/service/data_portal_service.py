import requests


def get_crime_data(target_data_portal):
    custom_headers = {'X-App-Token': target_data_portal.app_token}
    response = requests.get(target_data_portal.api_endpoint, headers=custom_headers)

    return response.json()
