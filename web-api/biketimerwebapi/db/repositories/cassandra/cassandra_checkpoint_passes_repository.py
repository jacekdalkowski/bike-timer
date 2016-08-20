import logging
from cassandra import ConsistencyLevel
from cassandra.query import BatchStatement
from ...entities.checkpoint_pass import CheckpointPass

logger = logging.getLogger('repositories')

class CassandraCheckpointPassesRepository:

    def __init__(self, cluster, session):
        self.cluster = cluster
        self.session = session

    def get_by_user(self, user_id):
        
        rows = self.session.execute("SELECT * FROM spots WHERE id=" + str(id))
        number_of_spots_with_id = sum(1 for row in rows)
        if number_of_spots_with_id > 0:
            if number_of_spots_with_id > 1:
                logger.warn('There is more than one spot with id=' + str(id))
            # TODO second query
            rows = session.execute("SELECT * FROM spots WHERE id=" + str(id))
            return Spot.row_to_entity(rows[0])
        else:
            pass

    def save_checkpoint_passes(self, checkpoint_pass_entities):
        insert_checkpoint_pass = self.session.prepare("INSERT INTO checkpoint_passes (id, user_id, time, checkpoint) VALUES (?, ?, ?, ?)")
        batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)

        for checkpoint_pass_entity in checkpoint_pass_entities:
            batch.add(insert_checkpoint_pass, [checkpoint_pass_entity.id, checkpoint_pass_entity.user_id, checkpoint_pass_entity.time, checkpoint_pass_entity.checkpoint])

        self.session.execute(batch)
