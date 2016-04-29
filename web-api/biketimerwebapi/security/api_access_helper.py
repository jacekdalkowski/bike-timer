import logging

logger = logging.getLogger('resources')

class ApiAccessHelper:

	@staticmethod
	def IsCurrentUser(idOrNoun, currentUserInfo):
		return idOrNoun.lower() == "me" or idOrNoun == str(currentUserInfo.id)

	@staticmethod
	def IsFriend(idOrNoun, currentUserInfo):
		return idOrNoun.lower() == "friends" or (idOrNoun in currentUserInfo.friends_ids)