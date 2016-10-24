from _tests.deployment.local_deployment import *
from _tests.deployment.remote_deployment import *
from _tests.facades.fb import *
from _tests.facades.identity import *
from _tests.facades.api import *
from _tests.facades.db import *
from _tests.scenarios.users_accounts import *
from _tests.scenarios.runs_single import *
from _tests.scenarios.runs_multiple import *

if __name__ == '__main__':
	#deployment_info = LocalDeployment.GetLocalDeployment()
	deployment_info = RemoteDeployment.GetRemoteDockerDeployment()

	db_facade = DbFacade(deployment_info.CqlshCommand)
	db_facade.clear_tables()
	db_facade.add_spot()

	users_accounts = UsersAccounts(deployment_info)
	#users_accounts.add_first_user();
	users_accounts.add_first_three_friends();

	runs_single = RunsSingle(deployment_info)
	runs_single.add_first_run_and_verify_tables()

	runs_multiple = RunsMultiple(deployment_info)
	runs_multiple.add_runs_for_one_user_and_verify_tables()



