
from ...entities.spot_entity import SpotEntity
from cassandra.cqlengine.management import sync_table

class CassandraSpotsRepository:
    def __init__(self):
        sync_table(SpotEntity)

    def get_all(self):
        all_spots = SpotEntity.objects
        return list(all_spots)

    def get_by_id(self,id):
        spot_query = SpotEntity.objects.filter(id=id)
        if spot_query.count() > 0:
            return spot_query[0]
        else:
            pass

