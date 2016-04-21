from datetime import datetime
from geo_point import GeoPoint
from track import Track

class Spot():

    def __init__(self):
        self.id = None
        self.name = None
        self.position = None
        self.tags = None
        self.tracks_current = None
        self.tracks_old = None

    @staticmethod
    def row_to_entity(row):
        spot_entity = Spot()
        spot_entity.id = row.id
        spot_entity.name = row.name
        spot_entity.position = GeoPoint.row_to_object(row.position)
        spot_entity.tags = row.tags
        spot_entity.tracks_current = [Track.row_to_object(track_row) for track_row in row.tracks_current]
        spot_entity.tracks_old = [Track.row_to_object(track_row) for track_row in row.tracks_old]
        return spot_entity

    def to_dict(self):
        dict_data = {};
        dict_data['id'] = str(self.id)
        dict_data['name'] = str(self.name)
        dict_data['position'] = self.position.to_dict() #str(self.position) + ' ' + str(type(self.position))
        dict_data['tags'] = [str(tag) for tag in self.tags]
        dict_data['tracks_old'] = [track.to_dict() for track in self.tracks_old]
        dict_data['tracks_current'] = [track.to_dict() for track in self.tracks_current]
        return dict_data
