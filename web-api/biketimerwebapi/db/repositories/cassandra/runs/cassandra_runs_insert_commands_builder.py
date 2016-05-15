import logging
from datetime import datetime
import uuid
from ..utils import Utils

logger = logging.getLogger('repositories')

class CassandraRunsInsertCommandsBuilder:

    def __init__(self):
        pass

    # TODO create stored procedures as far as Cassandra supports
    def get_command_to_insert_into_all_tables(self, spot_object, run_object):
        run_id = uuid.uuid1()
        c0 = self.get_command_to_insert_into_runs_by_user_spot_date(spot_object, run_object, run_id)
        c1 = self.get_command_to_insert_into_runs_by_user_date(spot_object, run_object, run_id)
        c2 = self.get_command_to_insert_into_runs_by_user_segment_date(spot_object, run_object, run_id)
        c3 = self.get_command_to_insert_into_runs_by_spot_user_date(spot_object, run_object, run_id)
        c4 = self.get_command_to_insert_into_runs_by_segment_date_time(spot_object, run_object, run_id)
        c5 = self.get_command_to_insert_into_runs_by_segment_user_date(spot_object, run_object, run_id)
        c6 = self.get_command_to_insert_into_runs_by_segment_time(spot_object, run_object, run_id)
        c7 = self.get_command_to_insert_into_runs_by_id(spot_object, run_object, run_id)
        return run_id, [c0, c1, c2, c3, c4, c5, c6, c7]

    def get_command_to_insert_into_runs_by_user_spot_date(self, spot_object, run_object, run_id):
        run_object_def = self.get_run_object_def_query_part(spot_object, run_object, run_id)
        return ('INSERT INTO runs_by_user_spot_date(id, user_id, spot_id, time_start, run_info) ' +
                'VALUES (' + str(run_id) + ', ' +
                str(run_object.user_id) + ', ' +
                str(spot_object.id) + ', ' +
                Utils.str_to_cassandra_time(str(run_object.time_start)) + ', ' +
                run_object_def + 
                ');')

    def get_command_to_insert_into_runs_by_user_date(self, spot_object, run_object, run_id):
        run_object_def = self.get_run_object_def_query_part(spot_object, run_object, run_id)
        return ('INSERT INTO runs_by_user_date(id, user_id, time_start, run_info) ' +
                'VALUES (' + str(run_id) + ', ' +
                str(run_object.user_id) + ', ' +
                Utils.str_to_cassandra_time(str(run_object.time_start)) + ', ' +
                run_object_def +
                ');')

    def get_command_to_insert_into_runs_by_user_segment_date(self, spot_object, run_object, run_id):
        run_object_def = self.get_run_object_def_query_part(spot_object, run_object, run_id)
        return ('INSERT INTO runs_by_user_segment_date(id, user_id, segment_id, time_start, run_info) ' +
                'VALUES (' + str(run_id) + ', ' +
                str(run_object.user_id) + ', ' +
                str(run_object.segment.id) + ', ' +
                Utils.str_to_cassandra_time(str(run_object.time_start)) + ', ' +
                run_object_def +
                ');')

    def get_command_to_insert_into_runs_by_spot_user_date(self, spot_object, run_object, run_id):
        run_object_def = self.get_run_object_def_query_part(spot_object, run_object, run_id)
        return ('INSERT INTO runs_by_spot_user_date(id, spot_id, user_id, time_start, run_info) ' +
                'VALUES (' + str(run_id) + ', ' +
                str(spot_object.id) + ', ' +
                str(run_object.user_id) + ', ' +
                Utils.str_to_cassandra_time(str(run_object.time_start)) + ', ' +
                run_object_def + 
                ');')

    def get_command_to_insert_into_runs_by_segment_date_time(self, spot_object, run_object, run_id):
        run_object_def = self.get_run_object_def_query_part(spot_object, run_object, run_id)
        return ('INSERT INTO runs_by_segment_date_time(id, segment_id, time_start, time_span_ms, run_info) ' +
                'VALUES (' + str(run_id) + ', ' +
                str(run_object.segment.id) + ', ' +
                Utils.str_to_cassandra_time(str(run_object.time_start)) + ', ' +
                str(run_object.time_span_ms) + ', ' +
                run_object_def +
                ');')

    def get_command_to_insert_into_runs_by_segment_user_date(self, spot_object, run_object, run_id):
        run_object_def = self.get_run_object_def_query_part(spot_object, run_object, run_id)
        return ('INSERT INTO runs_by_segment_user_date(id, segment_id, user_id, time_start, run_info) ' +
               'VALUES (' + str(run_id) + ', ' +
                str(run_object.segment.id) + ', ' +
                str(run_object.user_id) + ', ' +
                Utils.str_to_cassandra_time(str(run_object.time_start)) + ', ' +
                run_object_def +
                ');')

    def get_command_to_insert_into_runs_by_segment_time(self, spot_object, run_object, run_id):
        run_object_def = self.get_run_object_def_query_part(spot_object, run_object, run_id)
        return ('INSERT INTO runs_by_segment_time(id, segment_id, time_span_ms, time_start, run_info) ' +
               'VALUES (' + str(run_id) + ', ' +
                str(run_object.segment.id) + ', ' +
                str(run_object.time_span_ms) + ', ' +
                Utils.str_to_cassandra_time(str(run_object.time_start)) + ', ' +
                run_object_def + 
                ');')

    def get_command_to_insert_into_runs_by_id(self, spot_object, run_object, run_id):
        run_object_def = self.get_run_object_def_query_part(spot_object, run_object, run_id)
        return ('INSERT INTO runs_by_id(id, run_info) ' +
                'VALUES (' + str(run_id) + ', ' +
                run_object_def + 
                ');')

    def get_run_object_def_query_part(self, spot_object, run_object, run_id):
        return ('{ ' +
                '   id: ' + str(run_id) + ',' +
                '   user_id: ' + str(run_object.user_id) + ', ' +
                '   user_bt_name: \'' + run_object.user_bt_name + '\', ' +
                '   segment: { ' +
                '       id: ' + str(run_object.segment.id) + ', ' +
                '       name: \'' + run_object.segment.name + '\', '
                '       location_start: ' +
                '       { ' +
                '           id: ' + str(run_object.segment.location_start.id) + ', ' +
                '           location: { la: ' + str(run_object.segment.location_start.location.la) + ', lo: ' + str(run_object.segment.location_start.location.lo) + ' } ' +
                '       }, ' +
                '       location_stop: ' +
                '       { ' +
                '           id: ' + str(run_object.segment.location_stop.id) + ', ' +
                '           location: { la: ' + str(run_object.segment.location_stop.location.la) + ', lo: ' + str(run_object.segment.location_stop.location.lo) + ' } ' +
                '       }, ' +
                '       valid_time_start: ' + Utils.str_to_cassandra_time(str(run_object.segment.valid_time_start)) + ', ' +
                '       valid_time_stop: 0 ' +
                '   }, ' +
                '   time_start: ' + Utils.str_to_cassandra_time(str(run_object.time_start)) + ', ' +
                '   time_stop: ' + str(Utils.str_to_cassandra_time(str(run_object.time_stop))) + ', ' +
                '   time_span_ms: ' + str(run_object.time_span_ms) +
                '}')



