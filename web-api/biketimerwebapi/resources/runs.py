import logging
import json
from flask import Response
from flask import jsonify
from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity
from flask_injector import FlaskInjector
from injector import inject
from ..db.repositories.repositories_definitions import RunsRepository

logger = logging.getLogger('resources')

class Runs(Resource):

    method_decorators = [jwt_required()] 

    @inject(runs_repository=RunsRepository)
    def __init__(self, runs_repository):
        logger.debug('Runs.__init__(self, runs_repository)')
        self.runs_repository = runs_repository
    
    def get(self, id):
        query_params = parser.parse_args()
        logger.debug('Runs.get(self, args: ' + str(query_params) + ')')
        #return Response(json.dumps(spot.to_dict()),  mimetype='application/json')
        return {'yo', 'kfc'}, 404

    def post(self):
        logger.debug('Runs.post(self): invoked');
        pass