import logging
from segment_by_checkpoints import SegmentByCheckpoints

logger = logging.getLogger('cache')

class SpotsCache:
	
	def __init__(self, spots_repository):
		self.spots_repository = spots_repository

		# Dictionary of SegmentByCheckpoints, indexed by checkpoint_id
		self.checkpoints_by_id = None
		self.segments_by_checkpoints = None
		self.refresh()

	def refresh(self):
		logger.info('Cache refreshing started.')
		all_spots = self.spots_repository.get_all()
		checkpoints_by_id = self.load_checkpoints_to_dict(all_spots)
		segments_by_checkpoints = self.convert_spots_to_segments_by_checkpoints(all_spots)

		# deliberately not using any locks
		self.checkpoints_by_id = checkpoints_by_id
		self.segments_by_checkpoints = segments_by_checkpoints

		logger.info('Cache refreshing finished.')

	def find_checkpoint_by_id(self, checkpoint_id):
		return self.checkpoints_by_id[checkpoint_id]

	def find_segment_by_checkpoints(self, start_checkpoint_id, stop_checkpoint_id):
		if not start_checkpoint_id in self.segments_by_checkpoints:
			logger.warn('Could not find segment with start checkpoint id: ' + str(start_checkpoint_id))
			return
		segment_by_checkpoint = self.segments_by_checkpoints[start_checkpoint_id]
		if segment_by_checkpoint.checkpoint_stop.id != stop_checkpoint_id:
			logger.warn('Segment''s stop checkpoint id mismatch. Requested start_checkpoint_id ' + str(start_checkpoint_id) + ' requested stop_checkpoint_id: ' + str(stop_checkpoint_id))
			return 
		return segment_by_checkpoint

	def load_checkpoints_to_dict(self, all_spots):
		checkpoints = {}
		for spot in all_spots:
			for current_track in spot.tracks_current:
				for current_segment in current_track.segments_current:
					if not current_segment.location_start.id in checkpoints:
						checkpoints[current_segment.location_start.id] = current_segment.location_start
					if not current_segment.location_stop.id in checkpoints:
						checkpoints[current_segment.location_stop.id] = current_segment.location_stop
		return checkpoints


	def convert_spots_to_segments_by_checkpoints(self, all_spots):
		segments_by_checkpoints = {}
		for spot in all_spots:
			for current_track in spot.tracks_current:
				for current_segment in current_track.segments_current:
					segment_by_checkpoints = SegmentByCheckpoints(current_segment, current_track, spot)
					segment_start_checkpoint_id = segment_by_checkpoints.checkpoint_start.id
					if segment_start_checkpoint_id in segments_by_checkpoints:
						logger.warning('Duplicate checkpoint id: ' + str(segment_start_checkpoint_id) + '. Cannot add segment at to cache.')
						continue;
					segments_by_checkpoints[segment_start_checkpoint_id] = segment_by_checkpoints
		return segments_by_checkpoints


