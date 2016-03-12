from functools import wraps
from flask import g, request, redirect, url_for, _request_ctx_stack
from injector import inject
from ..db.repositories.repositories_definitions import UsersRepository
from flask_jwt import JWTError

def roles_required(roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_entity = _request_ctx_stack.top.current_identity
            for required_role in roles:
            	if not required_role in user_entity.roles:
            		raise JWTError('Access Denied', 'User does not have required roles assigned.')
            return f(*args, **kwargs)
        return decorated_function
    return decorator