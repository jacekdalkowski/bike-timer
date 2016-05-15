import logging

logger = logging.getLogger('resources')

class ApiAccessHelper:

	@staticmethod
	def IsCurrentUser(idOrNoun, currentUserInfo):
		return idOrNoun.lower() == "me" or idOrNoun == str(currentUserInfo.id)

	@staticmethod
	def IsFriend(idOrNoun, currentUserInfo):
		return idOrNoun.lower() == "friends" or (idOrNoun in currentUserInfo.friends_ids)

	@staticmethod
	def is_run_of_user_or_friend(run, user_info):
		belongs_to_user = (run.user_id == user_info.id)
		belongs_to_friend = (run.user_id in user_info.friends_ids)
		return belongs_to_user or belongs_to_friend