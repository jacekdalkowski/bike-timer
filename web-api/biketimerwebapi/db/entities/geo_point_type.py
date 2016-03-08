from cassandra.cqlengine import columns
from cassandra.cqlengine.usertype import UserType

class GeoPointType(UserType):
    __type_name__ = 'geopoint'
    la = columns.Double()
    lo = columns.Double()

    def to_dict(self):
    	dict_data = {};
    	dict_data['la'] = float(self.la)
    	dict_data['lo'] = float(self.lo)
    	return dict_data