from geo_point import GeoPoint

class Checkpoint(object):
    
    def __init__(self):
        self.id = None
        self.location = None

    @staticmethod
    def row_to_object(row):
        checkpoint = Checkpoint()
        checkpoint.id = row.id
        checkpoint.location = GeoPoint.row_to_object(row.location)
        return checkpoint

    def to_dict(self):
        dict_data = {};
        dict_data['id'] = str(self.id)
        dict_data['location'] = self.location.to_dict()
        return dict_data