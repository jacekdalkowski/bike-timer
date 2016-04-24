from segment import Segment
from datetime import datetime

class Run:
    def __init__(self):
        self.id = None
    
    @staticmethod
    def row_to_object(row):
        run = Run()
        run.id = row.id
        run.user_id = row.user_id
        run.segment_id = row.segment_id
        run.time_start = row.time_start
        run.time_finish = row.time_finish
        run.time_span = row.time_span
        return run

    def to_dict(self):
        dict_data = {};
        dict_data['id'] = str(self.id)
        return dict_data