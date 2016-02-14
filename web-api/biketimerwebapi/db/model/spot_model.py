import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.models import Model

class SpotModel(Model):
    id      = columns.UUID(primary_key=True, default=uuid.uuid4)
    name 	= columns.Text(required=False)
    position = UserDefinedType(GeoPointType)
    tags 	= columns.List(columns.Text)