from _tests.deployment.local_deployment import *
from _tests.facades.fb import *
from _tests.facades.identity import *
from _tests.facades.api import *
from _tests.facades.db import *
from _tests.scenarios.users_accounts import *

if __name__ == '__main__':
	'''
	local_deployment = LocalDeployment.GetLocalDockerDeployment()

	fb_facade = FbFacade()
	aaron_access_token = fb_facade.request_access_token(fb_facade.test_users.AaronChase.id)

	identity_facade = IdentityFacade(local_deployment.IdentityEndpoint.Address, local_deployment.IdentityEndpoint.Port)
	bt_token = identity_facade.request_bt_token_for_fb_token(aaron_access_token)

	api_facade = ApiFacade(local_deployment.ApiEndpoint.Address, local_deployment.ApiEndpoint.Port)
	api_facade.request_user_me(bt_token)
	'''

	#db_facade = DbFacade()
	#db_facade.clear_tables()

	users_accounts = UsersAccounts(LocalDeployment.GetLocalDeployment())
	#users_accounts.add_first_user();
	users_accounts.add_first_three_friends();



