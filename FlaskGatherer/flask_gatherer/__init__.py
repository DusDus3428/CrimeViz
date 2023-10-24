import os
import json

from flask import Flask

# Factory class to create a flask app
# test_config is used to inject settings to make testing easier
def create_app(test_config=None):
    # Here the flask app is created
    # It needs to know where it's located to set up some paths, hence the __name__
    # instance_relative_config=True means that config files are relative to instance folder
    app = Flask(__name__, instance_relative_config=True)
    
    # If we are not testing, load settings from config.json
    # If we are testing, load them from test_config
    if test_config is not None:
        app.config.from_file('config.json', load=json.load)
    else:
        app.config.from_mapping(test_config)

    # We need to ensure that the instance folder exists
    # Flask does not created it automatically
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    return app