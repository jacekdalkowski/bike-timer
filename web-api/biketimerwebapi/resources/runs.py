import logging
import json
import dateutil.parser
import uuid
from flask import Response
from flask import request
from flask import jsonify
from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity
from flask_injector import FlaskInjector
from flask_restful import reqparse
from injector import inject
from ..db.repositories.repositories_definitions import RunsRepository
from ..db.entities.run import Run
from ..cache.cache_definitions import SpotsCacheKey
from ..security.api_access_helper import ApiAccessHelper

logger = logging.getLogger('resources')

class Runs(Resource):

    method_decorators = [jwt_required()] 

    @inject(runs_repository=RunsRepository, spots_cache=SpotsCacheKey)
    def __init__(self, runs_repository, spots_cache):
        logger.debug('Runs.__init__(self, runs_repository)')
        self.runs_repository = runs_repository
        self.spots_cache = spots_cache

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('user_id')
        parser.add_argument('segment_id')
        parser.add_argument('spot_id')
        parser.add_argument('time_start_min')
        parser.add_argument('time_start_max')
        query_params = parser.parse_args()
        logger.debug('Runs.get(self, args: ' + str(query_params) + ')')
        spot_provided = False
        segment_provided = False
        user_provided = False
        if 'id' in query_params and query_params['id'] != None:
            return self.get_by_id(query_params)
        if 'user_id' in query_params and query_params['user_id'] != None:
            return self.get_by_single_user(query_params)
        if 'segment_id' in query_params and query_params['segment_id'] != None:
            return self.get_by_single_segment(query_params)
        if 'spot_id' in query_params and query_params['spot_id'] != None:
            return self.get_by_single_spot(query_params)
        return {}, 400

    def get_by_id(self, query_params):
        logger.debug('Runs.get_by_id(self, query_params: ' + str(query_params) + ')')
        run = self.runs_repository.get_from_runs_by_id(query_params)
        if ApiAccessHelper.is_run_of_user_or_friend(run, current_identity):
            return Response(json.dumps(run.to_dict()),  mimetype='application/json')
        else:
            logger.debug('Runs.get_by_id: requested run does not belong to current user nor to his friends. Returning 401.')
            return {}, 401

    def get_by_single_user(self, query_params):
        logger.debug('Runs.get_by_single_user(self, query_params: ' + str(query_params) + ')')
        user_id = query_params['user_id']
        if not ApiAccessHelper.IsCurrentUser(user_id, current_identity) and not ApiAccessHelper.IsFriend(user_id, current_identity):
            logger.debug('Runs.get_by_single_user: user_id is not current user''s id nor friend''s id. Returning 401.')
            return {}, 401
        if 'segment_id' in query_params and query_params['segment_id'] != None:
            logger.debug('Invoking RunsRepository.get_from_runs_by_user_segment_date')
            runs = self.runs_repository.get_from_runs_by_user_segment_date(query_params, current_identity)
            logger.debug('RunsRepository.get_from_runs_by_user_segment_date returned: ' + str(len(runs)) + ' entities.')
            response_data = [r.to_dict() for r in runs]
            return Response(json.dumps(response_data),  mimetype='application/json')
        if 'spot_id' in query_params and query_params['spot_id'] != None:
            logger.debug('Invoking RunsRepository.get_from_runs_by_user_spot_date')
            runs = self.runs_repository.get_from_runs_by_user_spot_date(query_params, current_identity)
            logger.debug('RunsRepository.get_from_runs_by_user_spot_date returned: ' + str(len(runs)) + ' entities.')
            response_data = [r.to_dict() for r in runs]
            return Response(json.dumps(response_data),  mimetype='application/json')       
        logger.debug('Invoking RunsRepository.get_from_runs_by_user_date')
        runs = self.runs_repository.get_from_runs_by_user_date(query_params, current_identity)
        logger.debug('RunsRepository.get_from_runs_by_user_date returned: ' + str(len(runs)) + ' entities.')
        response_data = [r.to_dict() for r in runs]
        return Response(json.dumps(response_data),  mimetype='application/json') 

    def get_by_single_segment(self, query_params):
        logger.debug('Runs.get_by_single_segment(self, query_params: ' + str(query_params) + ')')
        segment_id = query_params['segment_id']
        if 'time_start_min' in query_params and query_params['time_start_min'] != None:
            time_start_min = query_params['time_start_min']
            logger.debug('Invoking RunsRepository.get_from_runs_by_segment_date_time')
            runs = self.runs_repository.get_from_runs_by_segment_date_time(query_params, current_identity)
            logger.debug('RunsRepository.get_from_runs_by_user_spot_date returned: ' + str(len(runs)) + ' entities.')
            response_data = [r.to_dict() for r in runs]
            return Response(json.dumps(response_data),  mimetype='application/json')
        if 'user_id' in query_params and query_params['user_id'] != None:
            user_id = query_params['user_id']
            if ApiAccessHelper.IsCurrentUser(user_id, current_identity) or ApiAccessHelper.IsFriend(user_id, current_identity):
                logger.debug('Invoking RunsRepository.get_from_runs_by_segment_user_date')
                runs = self.runs_repository.get_from_runs_by_segment_user_date(query_params, current_identity)
                logger.debug('RunsRepository.get_from_runs_by_segment_user_date returned: ' + str(len(runs)) + ' entities.')
                response_data = [r.to_dict() for r in runs]
                return Response(json.dumps(response_data),  mimetype='application/json')
            else:
                return {}, 401
        logger.debug('Invoking RunsRepository.get_from_runs_by_segment_date_time')
        runs = self.runs_repository.get_from_runs_by_segment_date_time(query_params, current_identity)
        logger.debug('RunsRepository.get_from_runs_by_segment_date_time returned: ' + str(len(runs)) + ' entities.')
        response_data = [r.to_dict() for r in runs]
        return Response(json.dumps(response_data),  mimetype='application/json')

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
        if request.data == None:
            return {}, 400
        data = request.data
        logger.debug('Runs.post(self) data: ' + data);
        raw_request_data = json.loads(data)
        logger.debug(str(type(raw_request_data)))
        runs_ids = []
        for raw_run in raw_request_data:
            run_entity, spot_entity = self.run_request_data_to_run_and_spot(raw_run)
            run_id = self.runs_repository.save_run(spot_entity, run_entity)   
            runs_ids.append(str(run_id))     
        return {'runs_ids': runs_ids}, 200

    def run_request_data_to_run_and_spot(self, raw_run):
        checkpoint_start_id = uuid.UUID(raw_run["checkpoint_start_id"])
        checkpoint_stop_id = uuid.UUID(raw_run["checkpoint_stop_id"])
        time_start = dateutil.parser.parse(raw_run["time_start"])
        time_stop = dateutil.parser.parse(raw_run["time_stop"])
        user_id = current_identity.id
        user_bt_name = current_identity.bt_name

        segment_by_checkpoint = self.spots_cache.find_segment_by_checkpoints(checkpoint_start_id, checkpoint_stop_id)
        if segment_by_checkpoint == None:
            # TODO this could potentially lead to DOS...
            # should refresh only once in some fixed time window
            self.spots_cache.refresh()
            segment_by_checkpoint = self.spots_cache.find_segment_by_checkpoints(checkpoint_start_id, checkpoint_stop_id)
            if segment_by_checkpoint == None:
                raise Exception("Could not find segment. Start checkpoint id: " + checkpoint_start_id + " stop checkpoint id: " + checkpoint_stop_id)

        run_entity = Run();
        run_entity.user_id = user_id
        run_entity.user_bt_name = user_bt_name
        run_entity.segment = segment_by_checkpoint.segment
        run_entity.time_start = time_start
        run_entity.time_stop = time_stop
        run_entity.time_span_ms = 1

        return run_entity, segment_by_checkpoint.spot
        







