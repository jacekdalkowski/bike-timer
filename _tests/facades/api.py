import requests
import json

class ApiFacade:

	def __init__(self, api_server_host, api_server_port):
		self.api_server_host = api_server_host
		self.api_server_port = api_server_port

	def request_user_me(self, bt_token):
		r = requests.get('http://' + self.api_server_host + ':' + self.api_server_port + '/User/Me', 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received /User/Me response: ' + r.text
