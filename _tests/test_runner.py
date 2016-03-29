from deployment.local_deployment import *
from facades.fb import *
from facades.identity import *

if __name__ == '__main__':

	local_deployment = LocalDeployment.GetLocalDockerDeployment()

	fb_facade = FbFacade()
	aaron_access_token = fb_facade.request_access_token(fb_facade.test_users.AaronChase.id)

	identity_facade = IdentityFacade(local_deployment.IdentityEndpoint.Address, local_deployment.IdentityEndpoint.Port)
	identity_facade.request_bt_token_for_fb_token(aaron_access_token)
