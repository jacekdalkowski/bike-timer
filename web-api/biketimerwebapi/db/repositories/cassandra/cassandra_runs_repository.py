import logging
from ...entities.run import Run

logger = logging.getLogger('repositories')

class CassandraRunsRepository:
    def __init__(self, cluster):
        self.cluster = cluster;

    #def get_all(self):
    #    #all_spots = SpotEntity.objects
    #    #return list(all_spots)
    #    session = self.cluster.connect('biketimer')
    #    rows = session.execute("SELECT * FROM spots")
    #    spots = [Spot.row_to_entity(row) for row in rows]
    #    return spots;

    #def get_by_id(self,id):
    #    session = self.cluster.connect('biketimer')
    #    rows = session.execute("SELECT * FROM spots WHERE id=" + str(id))
    #    number_of_spots_with_id = sum(1 for row in rows)
    #    if number_of_spots_with_id > 0:
    #        if number_of_spots_with_id > 1:
    #            logger.warn('There is more than one spot with id=' + str(id))
            # TODO second query
    #        rows = session.execute("SELECT * FROM spots WHERE id=" + str(id))
    #        return Spot.row_to_entity(rows[0])
    #    else:
    #        pass




