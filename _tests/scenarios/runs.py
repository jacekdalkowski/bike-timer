from ..deployment.local_deployment import *
from ..facades.fb import *
from ..facades.identity import *
from ..facades.api import *
from ..facades.db import *
import json

# TODO use some testing framework

class Runs:

	def __init__(self, deployment_info):
		self.deployment_info = deployment_info
		self.db_facade = DbFacade(deployment_info.CqlshCommand)
		self.fb_facade = FbFacade()
		self.identity_facade = IdentityFacade(self.deployment_info.IdentityEndpoint.Address, self.deployment_info.IdentityEndpoint.Port)
		self.api_facade = ApiFacade(self.deployment_info.ApiEndpoint.Address, self.deployment_info.ApiEndpoint.Port)

	def add_first_run(self):
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
		segment_id = '00000000-0000-0000-0000-000000000003'
		time_start_min = '2016-05-07'
		time_start_max = '2016-05-08'
		api_runs_response_raw = self.api_facade.get_runs_by_user_segment_date(bt_token, 
			aaron_account_info['id'], segment_id, time_start_min, time_start_max)
		print 'get_runs_by_user_segment_date response: '
		print str(api_runs_response_raw) + '\n\n'

		spot_id = '00000000-0000-0000-0000-000000000001'
		api_runs_response_raw = self.api_facade.get_runs_by_user_spot_date(bt_token, 
			aaron_account_info['id'], spot_id, time_start_min, time_start_max)
		print 'get_runs_by_user_spot_date response: '
		print str(api_runs_response_raw) + '\n\n'

		return

		api_runs_response_raw = self.api_facade.get_runs_by_user_date(bt_token, 
			aaron_account_info['id'], time_start_min, time_start_max)
		print 'get_runs_by_user_date response: '
		print str(api_runs_response_raw)

		return

		api_runs_response_raw = self.api_facade.get_runs_by_spot_user_date(bt_token, 
			spot_id, aaron_account_info['id'], time_start_min, time_start_max)
		print 'get_runs_by_spot_user_date response: '
		print str(api_runs_response_raw) + '\n\n'

		api_runs_response_raw = self.api_facade.get_runs_by_segment_date_time(bt_token, 
			segment_id, time_start_min, time_start_max)
		print 'get_runs_by_segment_date_time response: '
		print str(api_runs_response_raw) + '\n\n'

		api_runs_response_raw = self.api_facade.get_runs_by_segment_user_date(bt_token, 
			segment_id, aaron_account_info['id'], time_start_min, time_start_max)
		print 'get_runs_by_segment_user_date response: '
		print str(api_runs_response_raw) + '\n\n'

		api_runs_response_raw = self.api_facade.get_runs_by_segment_time(bt_token, 
			segment_id, time_start_min, time_start_max)
		print 'get_runs_by_segment_time response: '
		print str(api_runs_response_raw) + '\n\n'

	def get_and_compare_from_all_tables(self):
		pass

	

		
		

	




