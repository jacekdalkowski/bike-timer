from checkpoint import Checkpoint

class Segment:
    def __init__(self):
        self.id = None;
        self.name = None
        self.location_start = None
        self.location_stop = None
        self.valid_time_start = None
        self.valid_time_stop = None

    @staticmethod
    def row_to_object(row):
        segment = Segment()
        segment.id = row.id
        segment.name = row.name
        segment.location_start = Checkpoint.row_to_object(row.location_start)
        segment.location_stop = Checkpoint.row_to_object(row.location_stop)
        segment.valid_time_start = row.valid_time_start
        segment.valid_time_stop = row.valid_time_stop
        return segment

    def to_dict(self):
        dict_data = {};
        dict_data['id'] = str(self.id)
        dict_data['name'] = str(self.name)
        dict_data['location_start'] = self.location_start.to_dict()
        dict_data['location_stop'] = self.location_stop.to_dict()
        dict_data['valid_time_start'] = str(self.valid_time_start)
        dict_data['valid_time_stop'] = str(self.valid_time_stop)
        return dict_data