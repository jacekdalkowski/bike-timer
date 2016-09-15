import logging
from datetime import datetime
from ....entities.run import Run
from cassandra_runs_query_builder import CassandraRunsQueryBuilder
from cassandra_runs_insert_commands_builder import CassandraRunsInsertCommandsBuilder
from cassandra_runs_query_result_parser import CassandraRunsQueryResultParser

logger = logging.getLogger('repositories')

class CassandraRunsRepository:
    def __init__(self, cluster, session):
        self.cluster = cluster
        self.session = session
        self.query_builder = CassandraRunsQueryBuilder()
        self.query_result_parser = CassandraRunsQueryResultParser()
        self.insert_commands_builder = CassandraRunsInsertCommandsBuilder()

    def get_from_runs_by_id(self, query_params):
        run_id = query_params['id']
        query = self.query_builder.get_from_runs_by_id(run_id)
        logger.debug(query)
        rows_list = list(self.session.execute(query))
        if len(rows_list) == 0:
            logger.warn('No runs found for id: ' + str(run_id))
            return None
        elif len(rows_list) > 1:
            logger.warn('More than one row returned for run id: ' + str(run_id) + '. Falling back to first found.')
        run_object = rows_list[0]
        return Run.row_to_object(run_object)

    def get_from_runs_by_user_segment_date(self, query_params, current_identity):
        query = self.query_builder.get_from_runs_by_user_segment_date(query_params, current_identity)
        logger.debug(query)
        rows = self.session.execute(query)
        objects = self.query_result_parser.parse_from_runs_by_user_segment_date(rows)
        return objects

    def get_from_runs_by_user_spot_date(self, query_params, current_identity):
        query = self.query_builder.get_from_runs_by_user_spot_date(query_params, current_identity)
        logger.debug(query)
        rows = self.session.execute(query)
        objects = self.query_result_parser.parse_from_runs_by_user_spot_date(rows)
        return objects

    def get_from_runs_by_user_date(self, query_params, current_identity):
        query = self.query_builder.get_from_runs_by_user_date(query_params, current_identity)
        logger.debug(query)
        rows = self.session.execute(query)
        objects = self.query_result_parser.parse_from_runs_by_user_date(rows)
        return objects

    def get_from_runs_by_segment_date_time(self, query_params, current_identity):
        query = self.query_builder.get_from_runs_by_segment_date_time(query_params, current_identity)
        logger.debug(query)
        rows = self.session.execute(query)
        objects = self.query_result_parser.parse_from_runs_by_segment_date_time(rows)
        return objects

    def get_from_runs_by_segment_user_date(self, query_params, current_identity):
        query = self.query_builder.get_from_runs_by_segment_user_date(query_params, current_identity)
        logger.debug(query)
        rows = self.session.execute(query)
        objects = self.query_result_parser.parse_from_runs_by_segment_user_date(rows)
        return objects

    def get_from_runs_by_spot_user_date(self, query_params, current_identity):
        query = self.query_builder.get_from_runs_by_spot_user_date(query_params, current_identity)
        logger.debug(query)
        rows = self.session.execute(query)
        objects = self.query_result_parser.parse_from_runs_by_spot_user_date(rows)
        return objects

    def save_run(self, spot_object, run_object):
        run_id, queries = self.insert_commands_builder.get_command_to_insert_into_all_tables(spot_object, run_object)
        for query in queries:
            self.session.execute(query)
        return run_id




