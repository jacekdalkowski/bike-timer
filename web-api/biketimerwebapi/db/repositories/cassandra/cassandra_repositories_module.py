from injector import Module
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from cassandra.cqlengine.management import create_keyspace_simple, sync_table, sync_type
from cassandra.cqlengine.usertype import UserType
from ...entities.track_type import TrackType
from cassandra_users_repository import CassandraUsersRepository
from cassandra_spots_repository import CassandraSpotsRepository
from runs.cassandra_runs_repository import CassandraRunsRepository
from ..repositories_definitions import UsersRepository
from ..repositories_definitions import SpotsRepository
from ..repositories_definitions import RunsRepository

class CassandraRepositoriesModule(Module):

    def configure(self, binder):
        connection.setup(['cassandrahost'], 'biketimer', protocol_version=4)
        cluster = Cluster(['cassandrahost'])

        users_repository_instance = CassandraUsersRepository(cluster) 
        binder.bind(UsersRepository, to=users_repository_instance)

        spots_repository_instance = CassandraSpotsRepository(cluster) 
        binder.bind(SpotsRepository, to=spots_repository_instance)

        runs_repository_instance = CassandraRunsRepository(cluster) 
        binder.bind(RunsRepository, to=runs_repository_instance)