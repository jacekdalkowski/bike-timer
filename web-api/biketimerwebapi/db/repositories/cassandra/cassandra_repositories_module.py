from injector import Module
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from cassandra_spots_repository import CassandraSpotsRepository
from ..repositories_definitions import SpotsRepository

class CassandraRepositoriesModule(Module):
    def configure(self, binder):

        #cluster = Cluster(['127.0.0.1'])
        #session = cluster.connect('biketimer')

        connection.setup(['127.0.0.1'], 'biketimer', protocol_version=3)

        spots_repository_instance = CassandraSpotsRepository('session') 

        binder.bind(SpotsRepository, to=spots_repository_instance)