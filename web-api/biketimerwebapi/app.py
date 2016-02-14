import logging
import logging.config
from flask import Flask
from flask_restful import Api
from resources.spot import Spot

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
app = Flask(__name__)
api = Api(app)

logger.info('adding resource: /Spot');
api.add_resource(Spot, '/Spot', '/Spot/<string:id>')

if __name__ == '__main__':
    #app.run(debug=True)
    hostAddress = '0.0.0.0'
    port = 5001
    logger.info('starting app on host: ' + hostAddress + ':' + str(port));
    app.run(host=hostAddress, port=port)