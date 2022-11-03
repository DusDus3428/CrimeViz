from logging.config import dictConfig
from python_gatherer_app.model.target_data_portal import TargetDataPortal
from flask import Flask


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

la = TargetDataPortal(
    'Los Angeles',
    'https://data.lacity.org',
    10,
    'Crime Data from 2020 to Present',
    'https://data.lacity.org/resource/2nrs-mtv8.json'
)

flask_app = Flask(__name__)
