import logging
import json
from flask import Response
from flask import jsonify
from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity
from flask_injector import FlaskInjector
from injector import inject
from ..db.repositories.repositories_definitions import SpotsRepository

logger = logging.getLogger('resources')

class Spot(Resource):

    @inject(spots_repository=SpotsRepository)
    def __init__(self, spots_repository):
    	logger.debug('Spot.__init__(self, spots_repository)')
        self.spots_repository = spots_repository

    method_decorators = [jwt_required()] 
    def get(self, id):
        logger.debug('Spot.get(self, id=' + str(id) + ')')
        spot = self.spots_repository.get_by_id(id)
        if spot != None:
            return Response(json.dumps(spot.to_dict()),  mimetype='application/json')
        else:
            return {}, 404

    def post(self):
        logger.debug('Spot.post(self): invoked');
        pass