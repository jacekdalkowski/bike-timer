from deployment.local_deployment import *
from facades.fb import *
from facades.identity import *
from facades.api import *

if __name__ == '__main__':

	local_deployment = LocalDeployment.GetLocalDockerDeployment()

	fb_facade = FbFacade()
	aaron_access_token = fb_facade.request_access_token(fb_facade.test_users.AaronChase.id)

	identity_facade = IdentityFacade(local_deployment.IdentityEndpoint.Address, local_deployment.IdentityEndpoint.Port)
	bt_token = identity_facade.request_bt_token_for_fb_token(aaron_access_token)

	api_facade = ApiFacade(local_deployment.ApiEndpoint.Address, local_deployment.ApiEndpoint.Port)
	api_facade.request_user_me(bt_token)

