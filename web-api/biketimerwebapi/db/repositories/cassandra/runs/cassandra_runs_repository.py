import logging
from datetime import datetime
from ....entities.run import Run
from cassandra_runs_query_builder import CassandraRunsQueryBuilder
from cassandra_runs_insert_commands_builder import CassandraRunsInsertCommandsBuilder
from cassandra_runs_query_result_parser import CassandraRunsQueryResultParser

logger = logging.getLogger('repositories')

class CassandraRunsRepository:
    def __init__(self, cluster):
        self.cluster = cluster;
        self.query_builder = CassandraRunsQueryBuilder()
        self.query_result_parser = CassandraRunsQueryResultParser()
        self.insert_commands_builder = CassandraRunsInsertCommandsBuilder()

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

    #def get_by_spot_user_date(self, spot_id, user_id, day):
    #    session = self.cluster.connect('biketimer')
    #    query = "SELECT * FROM runs_by_spot_user_date WHERE spot_id=" + str(spot_id) + " and user_id=" + str(user_id);
    #    if day != None:
    #        day_string = day.strftime('%Y-%m-%d')
    #        day_plus_day = day + datetime.timedelta(days=1)
    #        day_plus_day_string = day_plus_day.strftime('%Y-%m-%d')
    #        query += " and time_start >='" + date_string + "' and time_start < '" + day_plus_day_string + "'"
    #    rows = session.execute(query)
    #    return [Run.row_to_object(r) for r in rows]

    def get_from_runs_by_user_segment_date(self, query_params, current_identity):
        query = self.query_builder.get_from_runs_by_user_segment_date(query_params, current_identity)
        session = self.cluster.connect('biketimer')
        rows = session.execute(query)
        objects = self.query_result_parser.parse_from_runs_by_user_segment_date(rows)
        return objects

    def get_from_runs_by_user_spot_date(self, query_params, current_identity):
        query = self.query_builder.get_from_runs_by_user_spot_date(query_params, current_identity)
        session = self.cluster.connect('biketimer')
        rows = session.execute(query)
        objects = self.query_result_parser.parse_from_runs_by_user_spot_date(rows)
        return objects

    def get_from_runs_by_user_date(self, query_params, current_identity):
        pass

    def get_from_runs_by_segment_date_time(self, query_params, current_identity):
        pass

    def get_from_runs_by_segment_user_date(self, query_params, current_identity):
        pass

    def get_from_runs_by_spot_user_date(self, query_params, current_identity):
        pass

    def save_run(self, spot_object, run_object):
        query = self.insert_commands_builder.get_command_to_insert_into_all_tables(spot_object, run_object)
        session = self.cluster.connect('biketimer')
        rows = session.execute(query)




