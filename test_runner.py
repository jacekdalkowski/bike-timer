from _tests.deployment.local_deployment import *
from _tests.facades.fb import *
from _tests.facades.identity import *
from _tests.facades.api import *
from _tests.facades.db import *
from _tests.scenarios.users_accounts import *
from _tests.scenarios.runs_single import *
from _tests.scenarios.runs_multiple import *

if __name__ == '__main__':
	deployment = LocalDeployment.GetLocalDeployment()

	users_accounts = UsersAccounts(deployment)
	#users_accounts.add_first_user();
	#users_accounts.add_first_three_friends();

	runs_single = RunsSingle(deployment)
	runs_single.add_first_run_and_verify_tables()

	#runs_multiple = RunsMultiple(deployment)



