from segment import Segment
from datetime import datetime

class Run(object):
    def __init__(self):
        self.id = None
        self.user_id = None
        self.user_bt_name = None
        self.segment = None
        self.time_start = None
        self.time_stop = None
        self.time_span_ms = None
    
    @staticmethod
    def row_to_object(row):
        run = Run()
        run.id = row.id
        run.user_id = row.run_info.user_id
        run.user_bt_name = row.run_info.user_bt_name
        run.segment = Segment.row_to_object(row.run_info.segment)
        print 'type of time start cell'
        print str(type(row.run_info.time_start))
        run.time_start = row.run_info.time_start
        run.time_stop = row.run_info.time_stop
        run.time_span_ms = row.run_info.time_span_ms
        return run

    def to_dict(self):
        dict_data = {};
        dict_data['id'] = str(self.id)
        dict_data['user_id'] = str(self.user_id)
        dict_data['user_bt_name'] = str(self.user_bt_name)
        dict_data['segment'] = self.segment.to_dict()
        dict_data['time_start'] = self.time_start.strftime('%Y-%m-%d %H:%M:%S.%f')
        dict_data['time_stop'] = self.time_stop.strftime('%Y-%m-%d %H:%M:%S.%f')
        dict_data['time_span_ms'] = str(self.time_span_ms)
        return dict_data