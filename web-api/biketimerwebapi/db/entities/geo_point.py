
class GeoPoint(object):
    def __init__(self):
        self.la = None
        self.lo = None

    @staticmethod
    def row_to_object(row):
        geo_point = GeoPoint()
        geo_point.la = row.la
        geo_point.lo = row.lo
        return geo_point

    def to_dict(self):
        dict_data = {};
        dict_data['la'] = float(self.la)
        dict_data['lo'] = float(self.lo)
        return dict_data