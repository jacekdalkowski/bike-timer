import logging
from ...entities.spot import Spot

logger = logging.getLogger('repositories')

class CassandraSpotsRepository:

    def __init__(self, cluster, session):
        self.cluster = cluster;
        self.session = session;

    def get_all(self):
        #all_spots = SpotEntity.objects
        #return list(all_spots)
        rows = self.session.execute("SELECT * FROM spots")
        spots = [Spot.row_to_entity(row) for row in rows]
        return spots;

    def get_by_id(self,id):
        rows = self.session.execute("SELECT * FROM spots WHERE id=" + str(id))
        number_of_spots_with_id = sum(1 for row in rows)
        if number_of_spots_with_id > 0:
            if number_of_spots_with_id > 1:
                logger.warn('There is more than one spot with id=' + str(id))
            # TODO second query
            rows = self.session.execute("SELECT * FROM spots WHERE id=" + str(id))
            return Spot.row_to_entity(rows[0])
        else:
            pass




