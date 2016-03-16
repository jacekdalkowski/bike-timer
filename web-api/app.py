import sys
import logging
import logging.config
import ConfigParser
from flask import Flask
from flask_injector import FlaskInjector
from biketimerwebapi.common.error_friendly_api import ErrorFriendlyApi
from biketimerwebapi.resources.user import User
from biketimerwebapi.resources.spot import Spot
from biketimerwebapi.resources.spots import Spots
from biketimerwebapi.security.token_validator import TokenValidator
from biketimerwebapi.db.repositories.cassandra.cassandra_repositories_module import CassandraRepositoriesModule


def SetupLogging():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)
    return logger

def SetupConfig(argv, logger):
    configFileName = ''
    if len(argv) < 2:
        configFileName = 'localhost.conf'
    else:
        configFileName = argv[1]
    logger.info('Using config file: ' + configFileName)
    config = ConfigParser.ConfigParser()
    config.read('_artifacts/configs/' + configFileName)
    return config

def SetupFlaskApp(logger):
    app = Flask(__name__)
    api = ErrorFriendlyApi(app)
    api.add_resource(User, '/User', '/User/<string:id>')
    api.add_resource(Spot, '/Spot', '/Spot/<string:id>')
    api.add_resource(Spots, '/Spots')
    return app

def SetupBootstraper(logger):
    flask_injector = FlaskInjector(app=app, modules=[CassandraRepositoriesModule])
    return flask_injector

def StartListener(app, config, logger):
    hostAddress = config.get('Binding', 'address')
    port = int(config.get('Binding', 'port'))
    logger.info('Starting app on host: ' + hostAddress + ':' + str(port));
    app.run(host=hostAddress, port=port) #debug=True


if __name__ == '__main__':
    logger = SetupLogging()
    config = SetupConfig(sys.argv, logger)
    app = SetupFlaskApp(logger)
    flask_injector = SetupBootstraper(logger)
    token_validator = TokenValidator(app, flask_injector)
    StartListener(app, config, logger)

