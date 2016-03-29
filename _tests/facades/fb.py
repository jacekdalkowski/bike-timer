import requests
import json

class FbTestUser:

	def __init__(self, id, name, surname, email):
		self.id = id
		self.name = name
		self.surname = surname
		self.email = email

class FbTestUsersSet:

	def __init__(self):
		self.AaronChase = FbTestUser('102083143527533', 'Aaron', 'Chase', 'aaron_ovyobaz_chase@tfbnw.net')
		self.StevePeat = FbTestUser('163260570733439', 'Steve', 'Peat', 'steve_wnqrvfg_peat@tfbnw.net')
		self.LoicBruni = FbTestUser('185810031810233', 'Loic', 'Bruni', 'loic_exsscar_bruni@tfbnw.net')


class FbFacade:

	app_id = '942813139123420' # BikeTimer - localhost
	application_token = None
	test_users = FbTestUsersSet()

	def request_and_save_application_token(self):
		r = requests.get('https://graph.facebook.com/oauth/access_token', 
			params={'client_id': self.app_id, 
			'client_secret': 'ed7d7d348ce71db97c60f85e40625737',
			'grant_type': 'client_credentials'})
		print 'Received application access token: ' + r.text[13:]
		self.application_token = r.text[13:]

	def request_access_token(self, test_user_id):
		if self.application_token == None:
			self.request_and_save_application_token()
		response = requests.get('https://graph.facebook.com/v2.5/' + self.app_id + '/accounts/test-users',
			params={'access_token': self.application_token})
		for user in response.json()['data']:
			if user['id'] == test_user_id:
				return user['access_token']
		raise Exception('No test user with id: ' + test_user_id)