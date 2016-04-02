import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.columns import *
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.usertype import UserType

class UserEntity(Model):
    __table_name__ = 'Users'
    id      = columns.UUID(primary_key=True, default=uuid.uuid4)
    fb_id 	= columns.Text(required=True)
    bt_name = columns.Text(required=True)
    email 	= columns.Text(required=True)
    fb_access_token = columns.Text(required=True)
    fb_name = columns.Text(required=True)
    fb_surname = columns.Text(required=True)
    roles   = columns.List(columns.Text)
    friends_ids = columns.List(columns.UUID)

    def to_dict(self):
        dict_data = {};
        dict_data['id'] = str(self.id)
        dict_data['fb_id'] = str(self.fb_id)
        dict_data['bt_name'] = str(self.bt_name)
        dict_data['email'] = str(self.email)
        #dict_data['fb_access_token'] = str(self.fb_access_token)
        dict_data['fb_name'] = str(self.fb_name)
        dict_data['fb_surname'] = str(self.fb_surname)
        dict_data['roles'] = [str(role) for role in self.roles]
        dict_data['friends'] = [str(friend_id) for friend_id in self.friends_ids]
        return dict_data
