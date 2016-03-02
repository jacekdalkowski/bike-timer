import logging
from flask import Flask
from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity

#logger = logging.getLogger('resources')
logger = logging.getLogger(__name__)


class Spot(Resource):
    method_decorators = [jwt_required()] 
    def get(self):
        logger.debug('get(self): invoked')
        # return flask.jsonify(**dict)
        pass
    def post(self):
        logger.debug('post(self): invoked');
        pass