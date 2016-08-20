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
from ..db.repositories.repositories_definitions import CheckpointPassesRepository
from ..cache.cache_definitions import SpotsCacheKey
from ..db.entities.checkpoint_pass import CheckpointPass
from ..checkpoint_passes_to_runs_computer_module import CheckpointPassesToRunsComputerKey

logger = logging.getLogger('resources')

class CheckpointPasses(Resource):

    method_decorators = [jwt_required()] 

    @inject(checkpoint_passes_repository=CheckpointPassesRepository, spots_cache=SpotsCacheKey, checkpoint_passes_to_runs_computer=CheckpointPassesToRunsComputerKey)
    def __init__(self, checkpoint_passes_repository, spots_cache, checkpoint_passes_to_runs_computer):
        logger.debug('CheckpointPasses.__init__(self, checkpoint_passes_repository, spots_cache, checkpoint_passes_to_runs_computer)')
        self.checkpoint_passes_repository = checkpoint_passes_repository
        self.spots_cache = spots_cache
        self.checkpoint_passes_to_runs_computer = checkpoint_passes_to_runs_computer

    def post(self):
        logger.debug('CheckpointPasses.post(self): invoked');
        if request.data == None:
            return {}, 400
        data = request.data
        logger.debug('CheckpointPasses.post(self) data: ' + data);
        raw_request_data = json.loads(data)
        logger.debug(str(type(raw_request_data)))

        current_user_id = current_identity.id
        get_checkpoint_by_id = lambda id_str: self.spots_cache.find_checkpoint_by_id(uuid.UUID(id_str))
        checkpoint_pass_entities = [CheckpointPass.request_data_to_object(raw_checkpoint_pass, current_user_id, get_checkpoint_by_id) for raw_checkpoint_pass in raw_request_data]
        saved_checkpoint_passes_ids = self.checkpoint_passes_repository.save_checkpoint_passes(checkpoint_pass_entities)   
        saved_runs_ids = self.checkpoint_passes_to_runs_computer.compute_and_save_runs(current_user_id, saved_checkpoint_passes_ids)
        
        return {
            'saved_checkpoint_passes': saved_checkpoint_passes_ids,
            'saved_runs': saved_runs_ids
            }, 200


