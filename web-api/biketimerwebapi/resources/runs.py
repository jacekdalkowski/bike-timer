import logging
import json
from flask import Response
from flask import jsonify
from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity
from flask_injector import FlaskInjector
from flask_restful import reqparse
from injector import inject
from ..db.repositories.repositories_definitions import RunsRepository

logger = logging.getLogger('resources')

class Runs(Resource):

    method_decorators = [jwt_required()] 

    @inject(runs_repository=RunsRepository)
    def __init__(self, runs_repository):
        logger.debug('Runs.__init__(self, runs_repository)')
        self.runs_repository = runs_repository
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('spot_id')
        parser.add_argument('user_id')
        query_params = parser.parse_args()
        logger.debug('Runs.get(self, args: ' + str(query_params) + ')')
        spot_provided = False
        segment_provided = False
        user_provided = False
        if 'spot_id' in query_params:
            return self.get_by_spot(query_params)
        if 'segment_id' in query_params:
            return self.get_by_segment(query_params)
        if 'user_id' in query_params:
            return self.get_by_user(query_params)
        return {}, 400

    def get_by_spot(self, query_params):
        spot_id = query_params['spot_id']
        user_id = query_params['user_id']
        runs = self.runs_repository.get_by_spot_user_date(spot_id, user_id, None)
        return Response(json.dumps([run.to_dict() for run in runs]),  mimetype='application/json')

    def get_by_segment(self, query_params):
        pass

    def get_by_user(self, query_params):
        pass

    def post(self):
        logger.debug('Runs.post(self): invoked');
        pass