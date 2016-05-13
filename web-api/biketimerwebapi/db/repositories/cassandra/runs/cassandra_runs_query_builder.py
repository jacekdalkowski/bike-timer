import logging
from datetime import datetime
from ..utils import Utils

logger = logging.getLogger('repositories')

class CassandraRunsQueryBuilder:

    def __init__(self):
        pass

    def get_from_runs_by_user_segment_date(self, query_params, current_identity):
        user_id = self.map_user_id_to_db_id(query_params['user_id'], current_identity)
        segment_id = query_params['segment_id']

        query = ('select * from runs_by_user_segment_date where user_id=' + user_id +
                ' and segment_id=' + segment_id)

        if 'time_start_min' in query_params:
            time_start_min_str = query_params['time_start_min']
            time_start_min = Utils.str_to_cassandra_time(time_start_min_str)
            query += (' and time_start >= ' + time_start_min)

        if 'time_start_max' in query_params:
            time_start_max_str = query_params['time_start_max']
            time_start_max = Utils.str_to_cassandra_time(time_start_max_str)
            query += (' and time_start < ' + time_start_max)

        return query

    def get_from_runs_by_user_spot_date(self, query_params, current_identity):
        user_id = self.map_user_id_to_db_id(query_params['user_id'], current_identity)
        spot_id = query_params['spot_id']
        
        query = ('select * from runs_by_user_spot_date where user_id=' + user_id +
                ' and spot_id=' + spot_id)
        if 'time_start_min' in query_params:
            time_start_min_str = query_params['time_start_min']
            time_start_min = Utils.str_to_cassandra_time(time_start_min_str)
            query += (' and time_start >= ' + time_start_min)

        if 'time_start_max' in query_params:
            time_start_max_str = query_params['time_start_max']
            time_start_max = Utils.str_to_cassandra_time(time_start_max_str)
            query += (' and time_start < ' + time_start_max)

        return query

    def get_from_runs_by_user_date(self, query_params, current_identity):
        user_id = self.map_user_id_to_db_id(query_params['user_id'], current_identity)
        spot_id = query_params['spot_id']
        
        query = ('select * from runs_by_user_date where user_id=' + user_id)
        if 'time_start_min' in query_params:
            time_start_min_str = query_params['time_start_min']
            time_start_min = Utils.str_to_cassandra_time(time_start_min_str)
            query += (' and time_start >= ' + time_start_min)

        if 'time_start_max' in query_params:
            time_start_max_str = query_params['time_start_max']
            time_start_max = Utils.str_to_cassandra_time(time_start_max_str)
            query += (' and time_start < ' + time_start_max)

        return query

    def get_from_runs_by_segment_date_time(self, query_params, current_identity):
        pass

    def get_from_runs_by_segment_user_date(self, query_params, current_identity):
        pass

    def get_from_runs_by_spot_user_date(self, query_params, current_identity):
        pass

    def map_user_id_to_db_id(self, user_id, current_identity):
        if user_id.lower() == 'me':
            return str(current_identity.id)
        else:
            return user_id



