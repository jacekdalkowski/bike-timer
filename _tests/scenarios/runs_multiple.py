from ..deployment.local_deployment import *
from ..facades.fb import *
from ..facades.identity import *
from ..facades.api import *
from ..facades.db import *
import json

# TODO use some testing framework

class RunsMultiple:

	def __init__(self, deployment_info):
		self.deployment_info = deployment_info
		self.db_facade = DbFacade(deployment_info.CqlshCommand)
		self.fb_facade = FbFacade()
		self.identity_facade = IdentityFacade(self.deployment_info.IdentityEndpoint.Address, self.deployment_info.IdentityEndpoint.Port)
		self.api_facade = ApiFacade(self.deployment_info.ApiEndpoint.Address, self.deployment_info.ApiEndpoint.Port)

	def add_runs_for_one_user_and_verify_tables(self):
		self.db_facade.clear_tables()
		self.db_facade.add_spot()

		# Register / login Aaron.
		aaron_access_token = self.fb_facade.request_access_token(self.fb_facade.test_users.AaronChase.id)
		bt_token = self.identity_facade.request_bt_token_for_fb_token(aaron_access_token)
		# Get Aaron account.
		aaron_account_info = self.api_facade.get_user_me(bt_token)
		assert aaron_account_info['bt_name'] == 'Aaron Chase' 

		# Submit runs
		

	def post_one_run(self, user_bt_token, checkpoint_start_id, checkpoint_stop_id, time_start, time_stop):
		checkpoint_start_id = '00000000-0000-0000-0000-000000000005'
		checkpoint_stop_id = '00000000-0000-0000-0000-000000000006' 
		time_start = '2016-05-07T10:56:35.450686Z'
		time_stop = '2016-05-07T10:58:35.450686Z'
		post_run_response = self.api_facade.post_run(bt_token, 
				checkpoint_start_id, checkpoint_stop_id, 
				time_start, time_stop)
		run_id = post_run_response['runs_ids'][0]
		return run_id