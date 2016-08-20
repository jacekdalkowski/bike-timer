import logging
from cassandra import ConsistencyLevel
from cassandra.query import BatchStatement
from ...entities.checkpoint_pass import CheckpointPass

logger = logging.getLogger('repositories')

class CassandraCheckpointPassesRepository:

    def __init__(self, cluster, session):
        self.cluster = cluster
        self.session = session
        self.insert_into_checkpoint_passes_by_user_time = self.session.prepare("INSERT INTO checkpoint_passes_by_user_time (id, user_id, time, checkpoint) VALUES (?, ?, ?, ?)")
        self.insert_into_checkpoint_passes_by_user_id = self.session.prepare("INSERT INTO checkpoint_passes_by_user_id (id, user_id, time, checkpoint) VALUES (?, ?, ?, ?)")

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
        batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
        inserted_checkpoint_passes_ids = []

        for checkpoint_pass_entity in checkpoint_pass_entities:
            batch.add(self.insert_into_checkpoint_passes_by_user_time, [checkpoint_pass_entity.id, checkpoint_pass_entity.user_id, checkpoint_pass_entity.time, checkpoint_pass_entity.checkpoint])
            batch.add(self.insert_into_checkpoint_passes_by_user_id, [checkpoint_pass_entity.id, checkpoint_pass_entity.user_id, checkpoint_pass_entity.time, checkpoint_pass_entity.checkpoint])
            inserted_checkpoint_passes_ids.append(str(checkpoint_pass_entity.id))

        self.session.execute(batch)

        return inserted_checkpoint_passes_ids


