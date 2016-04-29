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
from ..security.api_access_helper import ApiAccessHelper

logger = logging.getLogger('resources')

class Runs(Resource):

    method_decorators = [jwt_required()] 

    @inject(runs_repository=RunsRepository)
    def __init__(self, runs_repository):
        logger.debug('Runs.__init__(self, runs_repository)')
        self.runs_repository = runs_repository

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
        logger.debug('Runs.get_by_single_user(self, query_params: ' + str(query_params) + ')')
        user_id = query_params['user_id']
        if not ApiAccessHelper.IsCurrentUser(user_id, current_identity) and not ApiAccessHelper.IsFriend(user_id, current_identity):
            logger.debug('Runs.get_by_single_user: user_id is not current user''s id nor friend''s id. Returning 401.')
            return {}, 401
        segment_id = query_params['segment_id']
        if segment_id != None:
            logger.debug('Invoking RunsRepository.get_from_runs_by_user_segment_date')
            runs = self.runs_repository.get_from_runs_by_user_segment_date(query_params, current_identity)
            logger.debug('RunsRepository.get_from_runs_by_user_segment_date returned: ' + str(len(runs)) + ' entities.')
            response_data = [r.to_dict() for r in runs]
            return Response(json.dumps(response_data),  mimetype='application/json')
        spot_id = query_params['spot_id']
        if spot_id != None:
            logger.debug('Invoking RunsRepository.get_from_runs_by_user_spot_date')
            runs = self.runs_repository.get_from_runs_by_user_spot_date(query_params, current_identity)
            logger.debug('RunsRepository.get_from_runs_by_user_spot_date returned: ' + str(len(runs)) + ' entities.')
            response_data = [r.to_dict() for r in runs]
            return Response(json.dumps(response_data),  mimetype='application/json')       
        date_id = query_params['date_id']
        if date_id != None:
            return self.runs_repository.get_from_runs_by_user_date(query_params, current_identity)
        return {}, 400

    def get_by_single_segment(self, query_params):
        logger.debug('Runs.get_by_single_segment(self, query_params: ' + str(query_params) + ')')
        segment_id = query_params['segment_id']
        time_start_min = query_params['time_start_min']
        if time_start_min != None:
            return self.runs_repository.get_from_runs_by_segment_date_time(query_params, current_identity)
        user_id = query_params['user_id']
        if user_id != None:
            if ApiAccessHelper.IsCurrentUser(user_id, current_identity) or ApiAccessHelper.IsFriend(user_id, current_identity):
                return self.runs_repository.get_from_runs_by_segment_user_date(query_params, current_identity)
            else:
                return {}, 401
        return self.runs_repository.get_from_runs_by_segment_date_time(query_params, current_identity)

    def get_by_single_spot(self, query_params):
        logger.debug('Runs.get_by_single_spot(self, query_params: ' + str(query_params) + ')')
        spot_id = query_params['spot_id']
        user_id = query_params['user_id']
        time_start_min = query_params['time_start_min']
        if spot_id != None and users_ids != None and time_start_min != None:
            if ApiAccessHelper.IsCurrentUser(user_id, current_identity) or ApiAccessHelper.IsFriend(user_id, current_identity):
                return self.runs_repository.get_from_runs_by_spot_user_date(query_params, current_identity)
            else:
                return {}, 401
        return {}, 400
        #runs = self.runs_repository.get_by_spot_user_date(spot_id, user_id, None)
        #return Response(json.dumps([run.to_dict() for run in runs]),  mimetype='application/json')

    def post(self):
        logger.debug('Runs.post(self): invoked');
        pass