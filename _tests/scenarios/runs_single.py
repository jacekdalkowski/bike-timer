import json
import dateutil.parser
from ..deployment.local_deployment import *
from ..facades.fb import *
from ..facades.identity import *
from ..facades.api import *
from ..facades.db import *
from ..utils import Utils

# TODO use some testing framework

class RunsSingle:

	def __init__(self, deployment_info):
		self.deployment_info = deployment_info
		self.db_facade = DbFacade(deployment_info.CqlshCommand)
		self.fb_facade = FbFacade()
		self.identity_facade = IdentityFacade(self.deployment_info.IdentityEndpoint.Address, self.deployment_info.IdentityEndpoint.Port)
		self.api_facade = ApiFacade(self.deployment_info.ApiEndpoint.Address, self.deployment_info.ApiEndpoint.Port)

	def add_first_run_and_verify_tables(self):

		# Register / login Aaron.
		aaron_access_token = self.fb_facade.request_access_token(self.fb_facade.test_users.AaronChase.id)
		bt_token = self.identity_facade.request_bt_token_for_fb_token(aaron_access_token)
		# Get Aaron account.
		aaron_account_info = self.api_facade.get_user_me(bt_token)
		assert aaron_account_info['bt_name'] == 'Aaron Chase' 

		test_segment = self.db_facade.spots.KoutyNadDesnou.tracks_current[0].segments_current[0]

		# Submit run.
		checkpoint_start_id = test_segment.location_start_checkpoint.id
		checkpoint_stop_id = test_segment.location_stop_checkpoint.id 
		time_start_string = '2016-05-19T10:56:35.000000Z'
		time_start = dateutil.parser.parse(time_start_string)
		time_stop_string = '2016-05-19T10:58:35.000000Z'
		time_stop = dateutil.parser.parse(time_stop_string)
		post_run_response = self.api_facade.post_run(bt_token, 
				checkpoint_start_id, checkpoint_stop_id, 
				time_start, time_stop)
		run_id = post_run_response['runs_ids'][0]

		# Query run tables.
		api_runs_response = self.api_facade.get_run_by_id(bt_token, run_id)
		print 'get_run_by_id response: '
		print str(api_runs_response) + '\n\n'
		Utils.assert_single_run([api_runs_response], run_id, aaron_account_info, time_start, time_stop, test_segment)

		segment_id = self.db_facade.spots.KoutyNadDesnou.tracks_current[0].segments_current[0].id
		time_start_min = '2016-05-07'
		time_start_max = '2016-05-08'
		api_runs_response = self.api_facade.get_runs_by_user_segment_date(bt_token, 
			aaron_account_info['id'], segment_id, time_start_min, time_start_max)
		print 'get_runs_by_user_segment_date response: '
		print str(api_runs_response) + '\n\n'
		Utils.assert_single_run(api_runs_response, run_id, aaron_account_info, time_start, time_stop, test_segment)

		spot_id = self.db_facade.spots.KoutyNadDesnou.id
		api_runs_response = self.api_facade.get_runs_by_user_spot_date(bt_token, 
			aaron_account_info['id'], spot_id, time_start_min, time_start_max)
		print 'get_runs_by_user_spot_date response: '
		print str(api_runs_response) + '\n\n'
		Utils.assert_single_run(api_runs_response, run_id, aaron_account_info, time_start, time_stop, test_segment)

		api_runs_response = self.api_facade.get_runs_by_user_date(bt_token, 
			aaron_account_info['id'], time_start_min, time_start_max)
		print 'get_runs_by_user_date response: '
		print str(api_runs_response) + '\n\n'
		Utils.assert_single_run(api_runs_response, run_id, aaron_account_info, time_start, time_stop, test_segment)

		api_runs_response = self.api_facade.get_runs_by_spot_user_date(bt_token, 
			spot_id, aaron_account_info['id'], time_start_min, time_start_max)
		print 'get_runs_by_spot_user_date response: '
		print str(api_runs_response) + '\n\n'
		Utils.assert_single_run(api_runs_response, run_id, aaron_account_info, time_start, time_stop, test_segment)

		api_runs_response = self.api_facade.get_runs_by_segment_date_time(bt_token, 
			segment_id, time_start_min, time_start_max)
		print 'get_runs_by_segment_date_time response: '
		print str(api_runs_response) + '\n\n'
		Utils.assert_single_run(api_runs_response, run_id, aaron_account_info, time_start, time_stop, test_segment)

		api_runs_response = self.api_facade.get_runs_by_segment_user_date(bt_token, 
			segment_id, aaron_account_info['id'], time_start_min, time_start_max)
		print 'get_runs_by_segment_user_date response: '
		print str(api_runs_response) + '\n\n'
		Utils.assert_single_run(api_runs_response, run_id, aaron_account_info, time_start, time_stop, test_segment)

		api_runs_response = self.api_facade.get_runs_by_segment_time(bt_token, 
			segment_id, time_start_min, time_start_max)
		print 'get_runs_by_segment_time response: '
		print str(api_runs_response) + '\n\n'
		Utils.assert_single_run(api_runs_response, run_id, aaron_account_info, time_start, time_stop, test_segment)

	
		

		
		

	




