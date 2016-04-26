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
from runs_helper import RunsDbHelper

logger = logging.getLogger('resources')

class Runs(Resource):

    method_decorators = [jwt_required()] 

    @inject(runs_repository=RunsRepository)
    def __init__(self, runs_repository):
        logger.debug('Runs.__init__(self, runs_repository)')
        self.runs_repository = runs_repository
        self.runs_db_helper = RunsDbHelper(self.runs_repository)
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id')
        parser.add_argument('segment_id')
        parser.add_argument('spot_id')
        query_params = parser.parse_args()
        logger.debug('Runs.get(self, args: ' + str(query_params) + ')')
        spot_provided = False
        segment_provided = False
        user_provided = False
        if 'user_id' in query_params:
            return self.get_by_single_user(query_params)
        if 'segment_id' in query_params:
            return self.get_by_single_segment(query_params)
        if 'spot_id' in query_params:
            return self.get_by_single_spot(query_params)
        return {}, 400

    def get_by_single_user(self, query_params):
        user_id = query_params['user_id']
        segment_id = query_params['segment_id']
        if segment_id != None:
            return self.runs_db_helper.get_from_runs_by_user_segment_date(query_params)
        spot_id = query_params['spot_id']
        if spot_id != None:
            return self.runs_db_helper.get_from_runs_by_user_spot_date(query_params)
        date_id = query_params['date_id']
        if date_id != None
            return self.runs_db_helper.get_from_runs_by_user_date(query_params)
        return {}, 400

    def get_by_single_segment(self, query_params):
        segment_id = query_params['segment_id']
        time_start_min = query_params['time_start_min']
        if time_start_min != None:
            return self.runs_db_helper.get_from_runs_by_segment_date_time(query_params)
        users_ids = query_params['user_id']
        if users_ids != None:
            return self.runs_db_helper.get_from_runs_by_segment_user_date(query_params)
        return get_from_runs_by_segment_date_time(query_params)

    def get_by_single_spot(self, query_params):
        spot_id = query_params['spot_id']
        users_ids = query_params['user_id']
        time_start_min = query_params['time_start_min']
        if spot_id != None and users_ids != None and time_start_min != None:
            return self.runs_db_helper.get_from_runs_by_spot_user_date(query_params)
        return {}, 400
        #runs = self.runs_repository.get_by_spot_user_date(spot_id, user_id, None)
        #return Response(json.dumps([run.to_dict() for run in runs]),  mimetype='application/json')

    def post(self):
        logger.debug('Runs.post(self): invoked');
        pass