from flask import Flask
from flask_jwt import JWT


class TokenValidator:
	def __init__(self, app):
		app.config['SECRET_KEY'] = '1234567890'
		jwt = JWT(app, self.authenticate, self.identity)

	def authenticate(username, password):
	    raise Exception('Authentication is not supported by this application')

	#@JWT.identity_handler
	def identity(self, payload):
	    bt_user_id = payload['btUserId']
	    return ''
