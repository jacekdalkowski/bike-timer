from flask import Flask
from flask_jwt import JWT
from ..db.repositories.repositories_definitions import UsersRepository

class TokenValidator:
	def __init__(self, app, flask_injector):
		app.config['SECRET_KEY'] = '1234567890'
		jwt = JWT(app, self.authenticate, self.identity)
		self.users_repository = flask_injector.injector.get(UsersRepository)

	def authenticate(username, password):
	    raise Exception('Authentication is not supported by this application')

	def identity(self, payload):
	    bt_user_id = payload['btUserId']
	    user_entity = self.users_repository.get_by_id(bt_user_id)
	    return user_entity
