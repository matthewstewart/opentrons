import logging
from logging.config import dictConfig
import os


data_dir = os.environ.get('APP_DATA_DIR', os.getcwd())
LOG_FILE_DIR = os.path.join(data_dir, 'logs')


logging_config = dict(
    version=1,
    formatters={
        'basic': {
            'format': '%(asctime)s %(name)s %(levelname)s [Line %(lineno)s]     %(message)s'  #NOQA
        }
    },
    handlers={
        'debug': {
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        'development': {
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        'opentrons-app': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(LOG_FILE_DIR, 'opentrons-app.log'),
            'maxBytes': 5000000,
            'backupCount': 3
        },
        'socketio': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(LOG_FILE_DIR, 'socketio.log'),
            'maxBytes': 5000000,
            'backupCount': 3
        },
        'opentrons': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'basic',
            'filename': os.path.join(LOG_FILE_DIR, 'opentrons.log'),
            'maxBytes': 5000000,
            'backupCount': 3
        },
    },
    loggers={
        'opentrons-app': {
         'handlers': ['opentrons-app'],
         'level': logging.INFO,
        },
        # 'socketio': {
        #  'handlers': ['socketio'],
        #  'level': logging.INFO,
        # },
        'opentrons': {
         'handlers': ['opentrons'],
         'level': logging.INFO,
        }
    }
)

dictConfig(logging_config)
