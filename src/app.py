from logging.config import fileConfig
from gunicorn.app.base import BaseApplication
from helper.config_helper import ConfigHelper
from config.server_config import ServerConfig

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import os
import logging
import connexion
import multiprocessing


def main():
    logger = logging.getLogger('app')
    server_properties = initialize_config()
    web_app = initialize_web_app()

    server_options = {
        'bind': f"0.0.0.0:{server_properties['port']}",
        'workers': server_properties['workers'] or number_of_workers(),
        'loglevel': server_properties['log_level']
    }

    logger.info("Initializing the application")
    Application(web_app, server_options).run()


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class Application(BaseApplication):

    def init(self, parser, opts, args):
        pass

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def initialize_config():
    path = os.path.dirname(os.path.realpath(__file__))
    fileConfig(f"{path}/config/log.ini")
    # fileConfig('./config/log.ini')
    config = ConfigHelper()

    return {
        'base_url': config.get('server', 'base_url'),
        'port': config.get('server', 'port'),
        'workers': config.get('server', 'workers'),
        'log_level': config.get('logging', 'level')
    }


def initialize_web_app():
    _app = connexion.FlaskApp(__name__, specification_dir='api/')
    flask_app = _app.app  # Unwrapping the Flask server from the connexion.FlaskApp object
    _rate_limiter = Limiter(
        flask_app,
        key_func=get_remote_address,
        default_limits=["1/second", "30 per hour"]
    )

    server_config = ServerConfig()
    server_config.set_rate_limiter(_rate_limiter)

    _app.add_api('openapi.yaml', base_path='/api')

    return _app


if __name__ == '__main__':
    main()
