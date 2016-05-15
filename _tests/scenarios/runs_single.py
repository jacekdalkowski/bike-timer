from ..deployment.local_deployment import *
from ..facades.fb import *
from ..facades.identity import *
from ..facades.api import *
from ..facades.db import *
import json

# TODO use some testing framework

class RunsSingle:

	def __init__(self, deployment_info):
		self.deployment_info = deployment_info
		self.db_facade = DbFacade(deployment_info.CqlshCommand)
		self.fb_facade = FbFacade()
		self.identity_facade = IdentityFacade(self.deployment_info.IdentityEndpoint.Address, self.deployment_info.IdentityEndpoint.Port)
		self.api_facade = ApiFacade(self.deployment_info.ApiEndpoint.Address, self.deployment_info.ApiEndpoint.Port)

	def add_first_run_and_verify_tables(self):
		self.db_facade.clear_tables()
		self.db_facade.add_spot()

		# Register / login Aaron.
		aaron_access_token = self.fb_facade.request_access_token(self.fb_facade.test_users.AaronChase.id)
		bt_token = self.identity_facade.request_bt_token_for_fb_token(aaron_access_token)
		# Get Aaron account.
		aaron_account_info = self.api_facade.get_user_me(bt_token)
		assert aaron_account_info['bt_name'] == 'Aaron Chase' 

		# Submit run.
		checkpoint_start_id = '00000000-0000-0000-0000-000000000005'
		checkpoint_stop_id = '00000000-0000-0000-0000-000000000006' 
		time_start = '2016-05-07T10:56:35.450686Z'
		time_stop = '2016-05-07T10:58:35.450686Z'
		post_run_response = self.api_facade.post_run(bt_token, 
				checkpoint_start_id, checkpoint_stop_id, 
				time_start, time_stop)
		run_id = post_run_response['runs_ids'][0]

		# Query run tables.
		api_runs_response = self.api_facade.get_run_by_id(bt_token, run_id)
		print 'get_run_by_id response: '
		print str(api_runs_response) + '\n\n'
		self.assert_single_run([api_runs_response], run_id, aaron_account_info)

		segment_id = '00000000-0000-0000-0000-000000000003'
		time_start_min = '2016-05-07'
		time_start_max = '2016-05-08'
		api_runs_response = self.api_facade.get_runs_by_user_segment_date(bt_token, 
			aaron_account_info['id'], segment_id, time_start_min, time_start_max)
		print 'get_runs_by_user_segment_date response: '
		print str(api_runs_response) + '\n\n'
		self.assert_single_run(api_runs_response, run_id, aaron_account_info)

		spot_id = '00000000-0000-0000-0000-000000000001'
		api_runs_response = self.api_facade.get_runs_by_user_spot_date(bt_token, 
			aaron_account_info['id'], spot_id, time_start_min, time_start_max)
		print 'get_runs_by_user_spot_date response: '
		print str(api_runs_response) + '\n\n'
		self.assert_single_run(api_runs_response, run_id, aaron_account_info)

		api_runs_response = self.api_facade.get_runs_by_user_date(bt_token, 
			aaron_account_info['id'], time_start_min, time_start_max)
		print 'get_runs_by_user_date response: '
		print str(api_runs_response) + '\n\n'
		self.assert_single_run(api_runs_response, run_id, aaron_account_info)

		api_runs_response = self.api_facade.get_runs_by_spot_user_date(bt_token, 
			spot_id, aaron_account_info['id'], time_start_min, time_start_max)
		print 'get_runs_by_spot_user_date response: '
		print str(api_runs_response) + '\n\n'
		self.assert_single_run(api_runs_response, run_id, aaron_account_info)

		api_runs_response = self.api_facade.get_runs_by_segment_date_time(bt_token, 
			segment_id, time_start_min, time_start_max)
		print 'get_runs_by_segment_date_time response: '
		print str(api_runs_response) + '\n\n'
		self.assert_single_run(api_runs_response, run_id, aaron_account_info)

		api_runs_response = self.api_facade.get_runs_by_segment_user_date(bt_token, 
			segment_id, aaron_account_info['id'], time_start_min, time_start_max)
		print 'get_runs_by_segment_user_date response: '
		print str(api_runs_response) + '\n\n'

		api_runs_response = self.api_facade.get_runs_by_segment_time(bt_token, 
			segment_id, time_start_min, time_start_max)
		print 'get_runs_by_segment_time response: '
		print str(api_runs_response) + '\n\n'

	def assert_single_run(self, api_runs_response, run_id, user_account_info):
		run_data = api_runs_response[0]
		assert run_data['id'] == run_id
		assert run_data['user_bt_name'] == user_account_info['bt_name']
		assert run_data['time_span_ms'] == '1'
		assert run_data['user_id'] == user_account_info['id']
		assert run_data['time_start'] == '2016-05-07 10:56:35.450000'
		assert run_data['time_stop'] == '2016-05-07 10:58:35.450000'
		assert run_data['segment']['id'] == '00000000-0000-0000-0000-000000000003'
		assert run_data['segment']['valid_time_start'] == '2013-05-13 09:41:11'
		assert run_data['segment']['valid_time_stop'] == '1970-01-01 00:00:00'
		assert run_data['segment']['name'] == 'Meadow'
		assert run_data['segment']['location_start']['id'] == '00000000-0000-0000-0000-000000000005'
		assert run_data['segment']['location_start']['location']['lo'] == 17.1077972
		assert run_data['segment']['location_start']['location']['la'] == 50.1010566
		assert run_data['segment']['location_stop']['id'] == '00000000-0000-0000-0000-000000000006'
		assert run_data['segment']['location_stop']['location']['lo'] == 17.1077972
		assert run_data['segment']['location_stop']['location']['la'] == 50.1010566

		
		

	




