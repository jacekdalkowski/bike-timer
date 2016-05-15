from db import *

class DbCommandBuilder:

	@staticmethod
	def create_tags_part(db_test_spot_tags):
		return str(db_test_spot_tags)

	@staticmethod
	def create_checkpoint_part(checkpoint):
		return ("{ "
				"	id: " + checkpoint.id + ", "
				"	location: { la: " + checkpoint.location_dict['la'] + ", lo: " + checkpoint.location_dict['lo'] + " } "
				"} ")

	@staticmethod
	def create_segments_command_part(segments_list):
		segment_strs = []
		for segment in segments_list:
			segment_strs.append(
				"{ "
				"	id: " + segment.id + ", "
				"	name: '" + segment.name + "', "
				"	location_start: " + DbCommandBuilder.create_checkpoint_part(segment.location_start_checkpoint) + ", "
				"	location_stop: " + DbCommandBuilder.create_checkpoint_part(segment.location_stop_checkpoint) + ", "
				"	valid_time_start: " + str(segment.valid_time_start) + ", "
				"	valid_time_stop: " + str(segment.valid_time_stop) + " "
				"} ");

		return ",".join(segment_strs)

	@staticmethod
	def create_tracks_command_part(tracks_list):
		track_strs = []
		for track in tracks_list:
			track_strs.append(
				"	{ "
				"		id: " + track.id + ", "
				"		name: '" + track.name + "', "
				"		segments_old: {" + DbCommandBuilder.create_segments_command_part(track.segments_old) + "},"
				"		segments_current: [" + DbCommandBuilder.create_segments_command_part(track.segments_current) + "], "
				"		valid_time_start: " + str(track.valid_time_start) +", "
				"		valid_time_stop: " + str(track.valid_time_stop) + " "
				"	} ")
		return ",".join(track_strs)

	@staticmethod
	def create_insert_spot_command(db_test_spot):
		add_spot_command = ("use biketimer; "
							"INSERT INTO spots(id, name, position, tags, tracks_old, tracks_current) "
							"VALUES (" + db_test_spot.id + ", '" + db_test_spot.name + "', "
							"{ la: " + db_test_spot.position['la'] + ", lo: " + db_test_spot.position['lo'] + " }, " + DbCommandBuilder.create_tags_part(db_test_spot.tags) + ", "
							"{ " + DbCommandBuilder.create_tracks_command_part(db_test_spot.tracks_old) + " }, "
							"{ " + DbCommandBuilder.create_tracks_command_part(db_test_spot.tracks_current) + "});")
		return add_spot_command

