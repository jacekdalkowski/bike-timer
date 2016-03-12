from injector import Module
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from cassandra_users_repository import CassandraUsersRepository
from cassandra_spots_repository import CassandraSpotsRepository
from ..repositories_definitions import UsersRepository
from ..repositories_definitions import SpotsRepository

class CassandraRepositoriesModule(Module):
    def configure(self, binder):
        connection.setup(['127.0.0.1'], 'biketimer', protocol_version=3)

        users_repository_instance = CassandraUsersRepository() 
        binder.bind(UsersRepository, to=users_repository_instance)

        spots_repository_instance = CassandraSpotsRepository() 
        binder.bind(SpotsRepository, to=spots_repository_instance)