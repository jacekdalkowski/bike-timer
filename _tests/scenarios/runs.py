from ..deployment.local_deployment import *
from ..facades.fb import *
from ..facades.identity import *
from ..facades.api import *
from ..facades.db import *

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
		run_data = self.api_facade.post_run(bt_token, 
				'00000000-0000-0000-0000-000000000005', '00000000-0000-0000-0000-000000000006', 
				'2016-05-07T10:56:35.450686Z', '2016-05-07T10:58:35.450686Z')
		print str(run_data)

	def get_and_compare_from_all_tables(self):
		pass

	

		
		

	




