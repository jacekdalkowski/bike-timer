from ..deployment.local_deployment import *
from ..facades.fb import *
from ..facades.identity import *
from ..facades.api import *
from ..facades.db import *

# TODO use some testing framework

class UsersAccounts:

	def __init__(self, deployment_info):
		self.deployment_info = deployment_info
		self.db_facade = DbFacade(deployment_info.CqlshCommand)
		self.fb_facade = FbFacade()
		self.identity_facade = IdentityFacade(self.deployment_info.IdentityEndpoint.Address, self.deployment_info.IdentityEndpoint.Port)
		self.api_facade = ApiFacade(self.deployment_info.ApiEndpoint.Address, self.deployment_info.ApiEndpoint.Port)

	def add_first_user(self):

		# Register Aaron.
		aaron_access_token = self.fb_facade.request_access_token(self.fb_facade.test_users.AaronChase.id)
		bt_token = self.identity_facade.request_bt_token_for_fb_token(aaron_access_token)

		# Get Aaron account.
		aaron_account_info = self.api_facade.get_user_me(bt_token)
		assert aaron_account_info['bt_name'] == 'Aaron Chase' 
		#Get Aaron friends
		print self.api_facade.get_user_friends(bt_token)

	def add_first_three_friends(self):

		# Register Aaron.
		aaron_fb_access_token = self.fb_facade.request_access_token(self.fb_facade.test_users.AaronChase.id)
		aaron_bt_access_token = self.identity_facade.request_bt_token_for_fb_token(aaron_fb_access_token)

		# Get Aaron account.
		aaron_account_info = self.api_facade.get_user_me(aaron_bt_access_token)
		assert aaron_account_info['bt_name'] == 'Aaron Chase' 
		assert len(aaron_account_info['friends']) == 0
		# Request Aaron friends. There should be none.
		aaron_friends = self.api_facade.get_user_friends(aaron_bt_access_token)
		assert len(aaron_friends) == 0

		# Register Steve.
		steve_fb_access_token = self.fb_facade.request_access_token(self.fb_facade.test_users.StevePeat.id)
		steve_bt_access_token = self.identity_facade.request_bt_token_for_fb_token(steve_fb_access_token)

		# Get Steve account.
		steve_account_info = self.api_facade.get_user_me(steve_bt_access_token)
		assert steve_account_info['bt_name'] == 'Steve Peat' 
		assert len(steve_account_info['friends']) == 1
		assert aaron_account_info['id'] in steve_account_info['friends']
		# Request Steve friends.
		steve_friends = self.api_facade.get_user_friends(steve_bt_access_token)
		assert len(steve_friends) == 1
		steve_friends_names = map(lambda f: f['bt_name'], steve_friends)
		assert 'Aaron Chase' in steve_friends_names

		# Aaron should now have Steve as a friend
		aaron_account_info = self.api_facade.get_user_me(aaron_bt_access_token)
		assert steve_account_info['id'] in aaron_account_info['friends']
		# Request Aaron friends.
		aaron_friends = self.api_facade.get_user_friends(aaron_bt_access_token)
		assert len(aaron_friends) == 1
		aaron_friends_names = map(lambda f: f['bt_name'], aaron_friends)
		assert 'Steve Peat' in aaron_friends_names

		# Register Loic.
		loic_fb_access_token = self.fb_facade.request_access_token(self.fb_facade.test_users.LoicBruni.id)
		loic_bt_access_token = self.identity_facade.request_bt_token_for_fb_token(loic_fb_access_token)

		# Get Loic account.
		loic_account_info = self.api_facade.get_user_me(loic_bt_access_token)
		assert loic_account_info['bt_name'] == 'Loic Bruni' 
		assert len(loic_account_info['friends']) == 2
		assert aaron_account_info['id'] in loic_account_info['friends']
		assert steve_account_info['id'] in loic_account_info['friends']
		# Check friends via /user/friends api
		loic_friends = self.api_facade.get_user_friends(loic_bt_access_token)
		assert len(loic_friends) == 2
		loic_friends_names = map(lambda f: f['bt_name'], loic_friends)
		assert 'Steve Peat' in loic_friends_names
		assert 'Aaron Chase' in loic_friends_names

		# Aaron should now have Loic and Steve as friends
		aaron_account_info = self.api_facade.get_user_me(aaron_bt_access_token)
		assert len(aaron_account_info['friends']) == 2
		assert steve_account_info['id'] in aaron_account_info['friends']
		assert loic_account_info['id'] in aaron_account_info['friends']
		# Check friends via /user/friends api
		aaron_friends = self.api_facade.get_user_friends(aaron_bt_access_token)
		assert len(aaron_friends) == 2
		aaron_friends_names = map(lambda f: f['bt_name'], aaron_friends)
		assert 'Steve Peat' in aaron_friends_names
		assert 'Loic Bruni' in aaron_friends_names

		# Steve should now have Loic and Aaron as friends
		steve_account_info = self.api_facade.get_user_me(steve_bt_access_token)
		assert len(steve_account_info['friends']) == 2
		assert aaron_account_info['id'] in steve_account_info['friends']
		assert loic_account_info['id'] in steve_account_info['friends']
		print self.api_facade.get_user_friends(steve_bt_access_token)
		# Check friends via /user/friends api
		steve_friends = self.api_facade.get_user_friends(steve_bt_access_token)
		assert len(steve_friends) == 2
		steve_friends_names = map(lambda f: f['bt_name'], steve_friends)
		assert 'Aaron Chase' in steve_friends_names
		assert 'Loic Bruni' in steve_friends_names






