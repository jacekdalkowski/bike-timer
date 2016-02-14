from cassandra.cqlengine import columns
from cassandra.cqlengine.usertype import UserType

class GeoPointType(UserType):
    la = columns.Double()
    lo = columns.Double()