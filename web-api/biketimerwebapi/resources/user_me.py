import logging
import json
from flask import Response
from flask import jsonify
from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity
from flask_injector import FlaskInjector
from injector import inject
from ..db.repositories.repositories_definitions import UsersRepository
from ..security.roles_validator import roles_required

logger = logging.getLogger('resources')

class UserMe(Resource):

    method_decorators = [jwt_required()] 

    @inject(users_repository=UsersRepository)
    def __init__(self, users_repository):
        logger.debug('UserMe.__init__(self, users_repository)')
        self.users_repository = users_repository

    @roles_required(['biker'])
    def get(self):
        logger.debug('UserMe.get(self)')
        return Response(json.dumps(current_identity.to_dict()),  mimetype='application/json')
