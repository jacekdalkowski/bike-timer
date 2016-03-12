import logging
from ...entities.spot_entity import SpotEntity
from cassandra.cqlengine.management import sync_table

logger = logging.getLogger('repositories')

class CassandraSpotsRepository:
    def __init__(self):
        sync_table(SpotEntity)

    def get_all(self):
        all_spots = SpotEntity.objects
        return list(all_spots)

    def get_by_id(self,id):
        spot_query = SpotEntity.objects.filter(id=id)
        number_of_spots_with_id = spot_query.count()
        if number_of_spots_with_id > 0:
            if number_of_spots_with_id > 1:
                logger.warn('There is more than one spot with id=' + str(id))
            return spot_query[0]
        else:
            pass

