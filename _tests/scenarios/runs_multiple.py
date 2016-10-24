from ..deployment.local_deployment import *
from ..facades.fb import *
from ..facades.identity import *
from ..facades.api import *
from ..facades.db import *
import json
import dateutil.parser
import datetime

# TODO use some testing framework

class RunsMultiple:

	def __init__(self, deployment_info):
		self.deployment_info = deployment_info
		self.db_facade = DbFacade(deployment_info.CqlshCommand)
		self.fb_facade = FbFacade()
		self.identity_facade = IdentityFacade(self.deployment_info.IdentityEndpoint.Address, self.deployment_info.IdentityEndpoint.Port)
		self.api_facade = ApiFacade(self.deployment_info.ApiEndpoint.Address, self.deployment_info.ApiEndpoint.Port)

	def add_runs_for_one_user_and_verify_tables(self):

		# Register / login users.
		aaron_fb_token = self.fb_facade.request_access_token(self.fb_facade.test_users.AaronChase.id)
		aaron_bt_token = self.identity_facade.request_bt_token_for_fb_token(aaron_fb_token)
		steve_fb_token = self.fb_facade.request_access_token(self.fb_facade.test_users.StevePeat.id)
		steve_bt_token = self.identity_facade.request_bt_token_for_fb_token(steve_fb_token)
		loic_fb_token = self.fb_facade.request_access_token(self.fb_facade.test_users.LoicBruni.id)
		loic_bt_token = self.identity_facade.request_bt_token_for_fb_token(loic_fb_token)
		# Get accounts.
		aaron_account_info = self.api_facade.get_user_me(aaron_bt_token)
		assert aaron_account_info['bt_name'] == 'Aaron Chase' 
		steve_account_info = self.api_facade.get_user_me(steve_bt_token)
		assert steve_account_info['bt_name'] == 'Steve Peat' 
		loic_account_info = self.api_facade.get_user_me(loic_bt_token)
		assert loic_account_info['bt_name'] == 'Loic Bruni' 

		first_segment = self.db_facade.spots.KoutyNadDesnou.tracks_current[0].segments_current[0]
		second_segment = self.db_facade.spots.KoutyNadDesnou.tracks_current[0].segments_current[1]

		# Submit runs
		# Aarons runs: |----|----| (08:01, 08:03, 08:05:05)
		# Steve runs:     |----|------| (08:02, 08:04, 08:07)
		# Loic runs:         |----|  |----|  (08:03:30, 08:05:30, 08:06:30, 08:08:30)
		first_run_start = dateutil.parser.parse('2016-05-19T08:01:00.000000Z')
		first_run_stop = first_run_start + datetime.timedelta(seconds=120)
		aaron_first_run_id = self.api_facade.post_run(aaron_bt_token, 
				first_segment.location_start_checkpoint.id, first_segment.location_stop_checkpoint.id,
				first_run_start, first_run_stop)

		second_run_start = first_run_stop
		second_run_stop = second_run_start + datetime.timedelta(seconds=125)
		aaron_second_run_id = self.api_facade.post_run(aaron_bt_token, 
				second_segment.location_start_checkpoint.id, second_segment.location_stop_checkpoint.id,
				second_run_start, second_run_stop)



		third_run_start = dateutil.parser.parse('2016-05-19T08:02:00.000000Z')
		third_run_stop = third_run_start + datetime.timedelta(seconds=120)
		steve_first_run_id = self.api_facade.post_run(steve_bt_token, 
				first_segment.location_start_checkpoint.id, first_segment.location_stop_checkpoint.id,
				third_run_start, third_run_stop)

		fourth_run_start = third_run_stop
		fourth_run_stop = third_run_start + datetime.timedelta(seconds=180)
		steve_second_run_id = self.api_facade.post_run(steve_bt_token, 
				second_segment.location_start_checkpoint.id, second_segment.location_stop_checkpoint.id,
				fourth_run_start, fourth_run_stop)



		fifth_run_start = dateutil.parser.parse('2016-05-19T08:03:30.000000Z')
		fifth_run_stop = fifth_run_start + datetime.timedelta(seconds=120)
		loic_first_run_id = self.api_facade.post_run(loic_bt_token, 
				first_segment.location_start_checkpoint.id, first_segment.location_stop_checkpoint.id,
				fifth_run_start, fifth_run_stop)

		sixth_run_start = dateutil.parser.parse('2016-05-19T08:06:30.000000Z')
		sixth_run_stop = fifth_run_start + datetime.timedelta(seconds=120)
		loic_second_run_id = self.api_facade.post_run(loic_bt_token, 
				second_segment.location_start_checkpoint.id, second_segment.location_stop_checkpoint.id,
				sixth_run_start, sixth_run_stop)


		

