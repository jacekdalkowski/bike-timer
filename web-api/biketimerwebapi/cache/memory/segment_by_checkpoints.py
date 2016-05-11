
class SegmentByCheckpoints:

	def __init__(self, segment, track, spot):
		self.checkpoint_start_id = segment.location_start.id
		self.checkpoint_stop_id = segment.location_stop.id
		self.segment = segment
		self.track = track
		self.spot = spot
