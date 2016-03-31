import requests
import json

class IdentityFacade:

	def __init__(self, identity_server_host, identity_server_port):
		self.identity_server_host = identity_server_host
		self.identity_server_port = identity_server_port

	def request_bt_token_for_fb_token(self, fb_token):
		response_raw = requests.post('http://' + self.identity_server_host + ':' + self.identity_server_port + '/token', 
			data={'grantType': 'facebook_token', 
			'accessToken': fb_token})
		print 'Received bt user access token response: ' + response_raw.text
		response_dict = json.loads(response_raw.text)
		print 'Received bt user access token: ' + response_dict['token']
		return response_dict['token']

