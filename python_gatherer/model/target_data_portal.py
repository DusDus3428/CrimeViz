class TargetDataPortal:
    def __init__(self, city, data_portal, request_interval, api_name, api_endpoint, app_token=''):
        self.city = city
        self.data_portal = data_portal
        self.request_interval = request_interval
        self.api_name = api_name
        self.api_endpoint = api_endpoint
        self.app_token = app_token
