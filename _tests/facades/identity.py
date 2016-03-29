import requests
import json

class IdentityFacade:

	def __init__(self, identity_server_host, identity_server_port):
		self.identity_server_host = identity_server_host
		self.identity_server_port = identity_server_port

	def request_bt_token_for_fb_token(self, fb_token):
		r = requests.post('http://' + self.identity_server_host + ':' + self.identity_server_port + '/token', 
			data={'grantType': 'facebook_token', 
			'accessToken': fb_token})
		print 'Received bt user access token: ' + r.text
