from segment import Segment

class Track:
    def __init__(self):
        self.id = None
        self.name = None
        self.segments_old = None
        self.segments_current = None
        self.valid_time_start = None
        self.valid_time_stop = None
    
    @staticmethod
    def row_to_object(row):
        track = Track()
        track.id = row.id
        track.name = row.name
        track.segments_old = [Segment.row_to_object(segment_row) for segment_row in row.segments_old]
        track.segments_current = [Segment.row_to_object(segment_row) for segment_row in row.segments_current]
        track.valid_time_start = row.valid_time_start
        track.valid_time_stop = row.valid_time_stop
        return track

    def to_dict(self):
        dict_data = {};
        dict_data['id'] = str(self.id)
        dict_data['name'] = str(self.name)
        dict_data['segments_old'] = [segment.to_dict() for segment in self.segments_old]
        dict_data['segments_current'] = [segment.to_dict() for segment in self.segments_current]
        dict_data['valid_time_start'] = str(self.valid_time_start)
        dict_data['valid_time_stop'] = str(self.valid_time_stop)
        return dict_data