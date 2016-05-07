from datetime import datetime
import dateutil.parser
import pytz

class Utils:
    @staticmethod
    def str_to_cassandra_time(dt_str):
        print dt_str
        dt = dateutil.parser.parse(dt_str)
        dt = Utils.ensure_offset_aware(dt)
        #epoch = datetime.utcfromtimestamp(0)
        epoch = datetime.fromtimestamp(0, pytz.utc)
        cassandra_time = (dt - epoch).total_seconds() * 1000.0
        return '%d' % cassandra_time

    @staticmethod
    def time_is_offset_naive(dt):
        return dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None

    @staticmethod
    def ensure_offset_aware(dt):
        if Utils.time_is_offset_naive(dt):
            return pytz.utc.localize(dt)
        else:
            return dt