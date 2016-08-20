import logging
from ...entities.user_entity import UserEntity
from cassandra.cqlengine.management import sync_table

logger = logging.getLogger('repositories')

class CassandraUsersRepository:
    def __init__(self, cluster, session):
        self.cluster = cluster;
        self.session = session;
        sync_table(UserEntity)

    def get_all(self):
        all_users = UserEntity.objects
        return list(all_users)

    def get_by_id(self, id):
        user_query = UserEntity.objects.filter(id=id)
        number_of_users_with_id = user_query.count()
        if number_of_users_with_id > 0:
            if number_of_users_with_id > 1:
                logger.warn('There is more than one user with id=' + str(id))
            return user_query[0]
        else:
            pass

    def get_friends(self, id):
        user = self.get_by_id(id)
        friends = UserEntity.objects.filter(id__in=user.friends_ids)
        return friends



