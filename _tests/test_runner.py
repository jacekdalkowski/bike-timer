from deployment.local_deployment import *

if __name__ == '__main__':
	local_deployment = LocalDeployment.GetLocalDockerDeployment()
	print local_deployment.ApiEndpoint.Address
	print local_deployment.ApiEndpoint.Port
