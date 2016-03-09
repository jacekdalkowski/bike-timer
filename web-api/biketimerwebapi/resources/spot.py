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
    def get(self):
        logger.debug('Spot.get(self)')
        all_spots = self.spots_repository.get_all()
        logger.debug(all_spots)
        response_data = [spot.to_dict() for spot in all_spots]
        logger.debug(response_data)
        return Response(json.dumps(response_data),  mimetype='application/json')

    def post(self):
        logger.debug('Spot.post(self): invoked');
        pass