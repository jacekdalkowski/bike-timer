import requests
import json

class ApiFacade:

	def __init__(self, api_server_host, api_server_port):
		self.api_server_host = api_server_host
		self.api_server_port = api_server_port

	def get_user_me(self, bt_token):
		r = requests.get('http://' + self.api_server_host + ':' + self.api_server_port + '/User/Me', 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received /User/Me response: ' + r.text
		return json.loads(r.text)

	def get_user_friends(self, bt_token):
		r = requests.get('http://' + self.api_server_host + ':' + self.api_server_port + '/User/Friends', 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received /User/Friends response: ' + r.text
		return json.loads(r.text)



	def get_runs_by_user_segment_date(self, bt_token, user_id, segment_id, time_start_min, time_start_max):
		url = ('http://' + self.api_server_host + ':' + self.api_server_port 
			+ '/Runs/?user_id=' + user_id + '&segment_id=' + segment_id)
		if time_start_min != None:
			url += ('&time_start_min=' + time_start_min)
		if time_start_max != None:
			url += ('&time_start_max=' + time_start_max)
		r = requests.get(url, 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received ' + url + ' response: ' + r.text
		return json.loads(r.text)

	def get_runs_by_user_spot_date(self, bt_token, user_id, spot_id, time_start_min, time_start_max):
		url = ('http://' + self.api_server_host + ':' + self.api_server_port 
			+ '/Runs/?user_id=' + user_id + '&spot_id=' + spot_id)
		if time_start_min != None:
			url += ('&time_start_min=' + time_start_min)
		if time_start_max != None:
			url += ('&time_start_max=' + time_start_max)
		r = requests.get(url, 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received ' + url + ' response: ' + r.text
		return json.loads(r.text)

	def get_runs_by_user_date(self, bt_token, user_id, time_start_min, time_start_max):
		url = 'http://' + self.api_server_host + ':' + self.api_server_port + '/Runs/?user_id=' + user_id
		if time_start_min != None:
			url += ('&time_start_min=' + time_start_min)
		if time_start_max != None:
			url += ('&time_start_max=' + time_start_max)
		r = requests.get(url, 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received ' + url + ' response: ' + r.text
		return json.loads(r.text)

	def get_runs_by_spot_user_date(self, bt_token, spot_id, user_id, time_start_min, time_start_max):
		url = ('http://' + self.api_server_host + ':' + self.api_server_port 
			+ '/Runs/?spot_id=' + spot_id + '&user_id=' + user_id)
		if time_start_min != None:
			url += ('&time_start_min=' + time_start_min)
		if time_start_max != None:
			url += ('&time_start_max=' + time_start_max)
		r = requests.get(url, 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received ' + url + ' response: ' + r.text
		return json.loads(r.text)

	# Skipping time param for now.
	def get_runs_by_segment_date_time(self, bt_token, segment_id, time_start_min, time_start_max):
		url = ('http://' + self.api_server_host + ':' + self.api_server_port 
			+ '/Runs/?segment_id=' + segment_id)
		if time_start_min != None:
			url += ('&time_start_min=' + time_start_min)
		if time_start_max != None:
			url += ('&time_start_max=' + time_start_max)
		r = requests.get(url, 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received ' + url + ' response: ' + r.text
		return json.loads(r.text)

	def get_runs_by_segment_user_date(self, bt_token, segment_id, user_id, time_start_min, time_start_max):
		url = ('http://' + self.api_server_host + ':' + self.api_server_port 
			+ '/Runs/?segment_id=' + segment_id
			+ '&user_id=' + user_id)
		if time_start_min != None:
			url += ('&time_start_min=' + time_start_min)
		if time_start_max != None:
			url += ('&time_start_max=' + time_start_max)
		r = requests.get(url, 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received ' + url + ' response: ' + r.text
		return json.loads(r.text)

	# Skipping time param for now.
	def get_runs_by_segment_time(self, bt_token, segment_id, time_start_min, time_start_max):
		url = ('http://' + self.api_server_host + ':' + self.api_server_port 
			+ '/Runs/?segment_id=' + segment_id)
		if time_start_min != None:
			url += ('&time_start_min=' + time_start_min)
		if time_start_max != None:
			url += ('&time_start_max=' + time_start_max)
		r = requests.get(url, 
			headers={'Authorization': 'JWT ' + bt_token})
		print 'Received ' + url + ' response: ' + r.text
		return json.loads(r.text)

	def post_run(self, bt_token, checkpoint_start_id, checkpoint_stop_id, time_start, time_stop):
		r = requests.post('http://' + self.api_server_host + ':' + self.api_server_port + '/Runs/', 
			headers={
				'Authorization': 'JWT ' + bt_token,
				'Content-Type': 'application/json'
			},
			data = json.dumps([{
				'checkpoint_start_id':'00000000-0000-0000-0000-000000000005',
				'checkpoint_stop_id': '00000000-0000-0000-0000-000000000006',
				'time_start': '2016-05-07T10:56:35.450686Z',
				'time_stop': '2016-05-07T10:58:35.450686Z'
			}]))
		print 'post run response: ' + r.text
		return json.loads(r.text)

