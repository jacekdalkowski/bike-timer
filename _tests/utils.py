from datetime import datetime
import dateutil.parser
import pytz

class Utils:

    @staticmethod
    def datetime_to_cassandra_time(dt):
        dt = Utils.ensure_offset_aware(dt)
        #epoch = datetime.utcfromtimestamp(0)
        epoch = datetime.fromtimestamp(0, pytz.utc)
        cassandra_time = (dt - epoch).total_seconds() * 1000.0
        return '%d' % cassandra_time

    @staticmethod
    def str_to_cassandra_time(dt_str):
        print dt_str
        dt = dateutil.parser.parse(dt_str)
        return datetime_to_cassandra_time(dt)

    @staticmethod
    def time_is_offset_naive(dt):
        return dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None

    @staticmethod
    def ensure_offset_aware(dt):
        if Utils.time_is_offset_naive(dt):
            return pytz.utc.localize(dt)
        else:
            return dt

    @staticmethod
    def assert_single_run(api_runs_response, run_id, user_account_info, time_start, time_stop, segment):
        run_data = api_runs_response[0]
        print str(run_data)
        assert run_data['id'] == run_id
        assert run_data['user_bt_name'] == user_account_info['bt_name']
        assert run_data['time_span_ms'] == '1'
        assert run_data['user_id'] == user_account_info['id']
        assert run_data['time_start'] == time_start.strftime("%Y-%m-%d %H:%M:%S.%f")

        assert run_data['time_stop'] == time_stop.strftime("%Y-%m-%d %H:%M:%S.%f")
        assert run_data['segment']['id'] == segment.id
        assert run_data['segment']['valid_time_start'] == segment.valid_time_start.strftime("%Y-%m-%d %H:%M:%S.%f")
        assert run_data['segment']['valid_time_stop'] == segment.valid_time_stop.strftime("%Y-%m-%d %H:%M:%S.%f")
        assert run_data['segment']['name'] == segment.name
        assert run_data['segment']['location_start']['id'] == segment.location_start_checkpoint.id
        assert str(run_data['segment']['location_start']['location']['la']) == segment.location_start_checkpoint.location_dict['la']
        assert str(run_data['segment']['location_start']['location']['lo']) == segment.location_start_checkpoint.location_dict['lo']
        assert run_data['segment']['location_stop']['id'] == segment.location_stop_checkpoint.id
        assert str(run_data['segment']['location_stop']['location']['la']) == segment.location_stop_checkpoint.location_dict['la']
        assert str(run_data['segment']['location_stop']['location']['lo']) == segment.location_stop_checkpoint.location_dict['lo']



        