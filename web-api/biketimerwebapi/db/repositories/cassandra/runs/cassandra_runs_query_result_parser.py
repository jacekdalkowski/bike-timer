import logging
from datetime import datetime
from ....entities.run import Run
from cassandra_runs_query_builder import CassandraRunsQueryBuilder

logger = logging.getLogger('repositories')

class CassandraRunsQueryResultParser:

    def __init__(self): 
        pass

    def parse_from_runs_by_user_segment_date(self, rows):
        return [Run.row_to_object(r) for r in rows]

    def parse_from_runs_by_user_spot_date(self, rows):
        return [Run.row_to_object(r) for r in rows]

    def parse_from_runs_by_user_date(self, rows):
        return [Run.row_to_object(r) for r in rows]

    def parse_from_runs_by_segment_date_time(self, rows):
        return [Run.row_to_object(r) for r in rows]

    def parse_from_runs_by_segment_user_date(self, rows):
        return [Run.row_to_object(r) for r in rows]

    def parse_from_runs_by_spot_user_date(self, rows):
        return [Run.row_to_object(r) for r in rows]