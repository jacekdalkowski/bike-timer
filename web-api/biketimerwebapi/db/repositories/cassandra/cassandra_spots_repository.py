
from ...entities.spot_entity import SpotEntity
from cassandra.cqlengine.management import sync_table

class CassandraSpotsRepository:
    def __init__(self, session):
        #self.session = session
        sync_table(SpotEntity)

    def get_all(self):
        #spots_rows = session.execute('SELECT id, name, position, tags FROM users')
        #for spots_rows in spots_rows:
        #    print spots_rows.id, spots_rows.name, spots_rows.position, spots_rows.tags
        all_spots = SpotEntity.objects
        return list(all_spots)

    def get_by_id(self):
        spot_row = session.execute('SELECT id, name, position, tags FROM users')

