import logging
from flask import Flask
from flask_restful import Resource

#logger = logging.getLogger('resources')
logger = logging.getLogger(__name__)


class Spot(Resource):
    def get(self):
    	logger.debug('get(self): invoked')
        # return flask.jsonify(**dict)
        pass
    def post(self):
    	logger.debug('post(self): invoked');
        pass