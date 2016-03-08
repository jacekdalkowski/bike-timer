import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.columns import *
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.usertype import UserType
from geo_point_type import GeoPointType

class SpotEntity(Model):
    __table_name__ = 'Spots'
    id      = columns.UUID(primary_key=True, default=uuid.uuid4)
    name 	= columns.Text(required=False)
    position = UserDefinedType(GeoPointType)
    tags 	= columns.List(columns.Text)

    def to_dict(self):
        dict_data = {};
        dict_data['id'] = str(self.id)
        dict_data['name'] = str(self.name)
        dict_data['position'] = self.position.to_dict() #str(self.position) + ' ' + str(type(self.position))
        dict_data['tags'] = [str(tag) for tag in self.tags]
        return dict_data
