
class SegmentByCheckpoints:

	def __init__(self, segment, track, spot):
		self.checkpoint_start = segment.location_start
		self.checkpoint_stop = segment.location_stop
		self.segment = segment
		self.track = track
		self.spot = spot
