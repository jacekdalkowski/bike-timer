import uuid
import dateutil.parser
from checkpoint import Checkpoint


class CheckpointPass(object):
    
    def __init__(self):
        self.id = None
        self.user_id = None
        self.time = None
        self.checkpoint = None

    @staticmethod
    def request_data_to_object(request_data, user_id, id_to_checkpoint):
        checkpoint_pass_object = CheckpointPass()
        checkpoint_pass_object.id = uuid.UUID(request_data["id"])
        checkpoint_pass_object.user_id = user_id
        checkpoint_pass_object.time = dateutil.parser.parse(request_data["time"])
        checkpoint_pass_object.checkpoint = id_to_checkpoint(request_data["checkpoint_id"])
        return checkpoint_pass_object

    @staticmethod
    def row_to_object(row):
        checkpoint_pass_object = CheckpointPass()
        checkpoint_pass_object.id = row.id
        checkpoint_pass_object.user_id = row.user_id
        checkpoint_pass_object.time = row.time
        checkpoint_pass_object.checkpoint = Checkpoint.row_to_object(row.checkpoint)
        return checkpoint_pass_object

    def to_dict(self):
        dict_data = {};
        dict_data['id'] = str(self.id)
        dict_data['user_id'] = str(self.user_id)
        dict_data['time'] = str(self.time)
        dict_data['checkpoint'] = str(self.checkpoint.to_dict())
        return dict_data