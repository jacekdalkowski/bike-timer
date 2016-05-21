import subprocess
from db_command_builder import DbCommandBuilder
import dateutil.parser

class DbTestCheckpoint:

	def __init__(self, id, location_dict):
		self.id = id
		self.location_dict = location_dict
		self.parent_segment = None

	def set_references_to_parents(self, parent):
		self.parent_segment = parent


class DbTestSegment:

	def __init__(self, id, name, location_start_checkpoint, location_stop_checkpoint, valid_time_start, valid_time_stop):
		self.id = id
		self.name = name
		self.location_start_checkpoint = location_start_checkpoint
		self.location_stop_checkpoint = location_stop_checkpoint
		self.valid_time_start = valid_time_start
		self.valid_time_stop = valid_time_stop
		self.parent_track = None

	def set_references_to_parents(self, parent):
		self.parent_track = parent
		self.location_start_checkpoint.set_references_to_parents(self)
		self.location_stop_checkpoint.set_references_to_parents(self)

class DbTestTrack:

	def __init__(self, id, name, segments_old_list, segments_current_list, valid_time_start, valid_time_stop):
		self.id = id
		self.name = name
		self.segments_old = segments_old_list
		self.segments_current = segments_current_list
		self.valid_time_start = valid_time_start
		self.valid_time_stop = valid_time_stop
		self.parent_spot = None

	def set_references_to_parents(self, parent):
		self.parent_spot = parent
		for segment_old in self.segments_old:
			segment_old.set_references_to_parents(self)
		for segment_current in self.segments_current:
			segment_current.set_references_to_parents(self)

class DbTestSpot:

	def __init__(self, id, name, position_dict, tags_list, tracks_old_list, tracks_current_list):
		self.id = id
		self.name = name
		self.position = position_dict
		self.tags = tags_list
		self.tracks_old = tracks_old_list
		self.tracks_current = tracks_current_list
		self.set_references_to_parents()

	def set_references_to_parents(self):
		for track_old in self.tracks_old:
			track_old.set_references_to_parents(self)
		for track_current in self.tracks_current:
			track_current.set_references_to_parents(self)

class DbTestSpotsSet:

	def __init__(self):
		self.KoutyNadDesnou = DbTestSpot('00000000-0000-0000-0000-000000000001', 'Kouty nad Desnou',
			{'la': '50.1010566', 'lo': '17.1077972'}, ['Kouty', 'Loucna'],
			[DbTestTrack('00000000-0000-0000-0000-000000000001', 'Chicken line', 
				[DbTestSegment(
					'00000000-0000-0000-0000-000000000001', 
					'Chicken line - First segment', 
					DbTestCheckpoint(
						'00000000-0000-0000-0000-000000000001',
						{ 'la': '50.1010566', 'lo': '17.1077972' }),
					DbTestCheckpoint(
						'00000000-0000-0000-0000-000000000002',
						{ 'la': '50.1010566','lo': '17.1077972' }),
					dateutil.parser.parse('1970-01-01 00:00:00+0000'),
					dateutil.parser.parse('1970-01-01 00:00:00+0000')
				)],
				[DbTestSegment(
					'00000000-0000-0000-0000-000000000002', 
					'Chicken line - Second segment', 
					DbTestCheckpoint(
						'00000000-0000-0000-0000-000000000003',
						{ 'la': '50.1010566', 'lo': '17.1077972' }),
					DbTestCheckpoint(
						'00000000-0000-0000-0000-000000000004',
						{ 'la': '50.1010566', 'lo': '17.1077972' }),
					dateutil.parser.parse('1970-01-01 00:00:00+0000'),
					dateutil.parser.parse('1970-01-01 00:00:00+0000')
				)],
				dateutil.parser.parse('1970-01-01 00:00:00+0000'),
				dateutil.parser.parse('1970-01-01 00:00:00+0000')
			)],
			[DbTestTrack('00000000-0000-0000-0000-000000000002', 'RED line', 
				[],
				[DbTestSegment(
					'00000000-0000-0000-0000-000000000003', 
					'RED line - Meadow', 
					DbTestCheckpoint(
						'00000000-0000-0000-0000-000000000005',
						{ 'la': '50.1010566', 'lo': '17.1077972' }),
					DbTestCheckpoint(
						'00000000-0000-0000-0000-000000000006',
						{ 'la': '50.1010566', 'lo': '17.1077972' }),
					dateutil.parser.parse('1970-01-01 00:00:00+0000'),
					dateutil.parser.parse('1970-01-01 00:00:00+0000')
				),
				DbTestSegment(
					'00000000-0000-0000-0000-000000000004', 
					'RED line - Forest', 
					DbTestCheckpoint(
						'00000000-0000-0000-0000-000000000007',
						{ 'la': '50.1010566', 'lo': '17.1077972' }),
					DbTestCheckpoint(
						'00000000-0000-0000-0000-000000000008',
						{ 'la': '50.1010566', 'lo': '17.1077972' }),
					dateutil.parser.parse('1970-01-01 00:00:00+0000'),
					dateutil.parser.parse('1970-01-01 00:00:00+0000')
				)],
				dateutil.parser.parse('1970-01-01 00:00:00+0000'),
				dateutil.parser.parse('1970-01-01 00:00:00+0000')
			)])

class DbFacade:

	def __init__(self, cqlshCommand):
		self.cqlshCommand = cqlshCommand
		self.spots = DbTestSpotsSet()

	def clear_tables(self):
		delete_from_tables_command = ("use biketimer; "
										"truncate users; "
										"truncate spots; "
										"truncate runs_by_user_segment_date; "
										"truncate runs_by_segment_date_time; "
										"truncate runs_by_user_spot_date; "
										"truncate runs_by_user_date; "
										"truncate runs_by_spot_user_date; "
										"truncate runs_by_segment_user_date; "
										"truncate runs_by_segment_time; "
										"truncate runs_by_id; ")
		p_echo_command = subprocess.Popen(['echo', delete_from_tables_command], stdout=subprocess.PIPE)
		p_cqlsh = subprocess.Popen(self.cqlshCommand, stdin=p_echo_command.stdout, stdout=subprocess.PIPE)
		out, err = p_cqlsh.communicate()
		print "Db command 'delete_from_tables_command' output: " + str(out)
		print "Db command 'delete_from_tables_command' error output: " + str(err)

	def add_spot(self):
		add_spot_command = DbCommandBuilder.create_insert_spot_command(self.spots.KoutyNadDesnou)
		p_echo_command = subprocess.Popen(['echo', add_spot_command], stdout=subprocess.PIPE)
		p_cqlsh = subprocess.Popen(self.cqlshCommand, stdin=p_echo_command.stdout, stdout=subprocess.PIPE)
		out, err = p_cqlsh.communicate()
		print "Db command 'add_spot_command' output: " + str(out)
		print "Db command 'add_spot_command' error output: " + str(err)

'''
	def add_spot(self):
		add_spot_command = ("use biketimer; "
							"INSERT INTO spots(id, name, position, tags, tracks_old, tracks_current) "
							"VALUES (00000000-0000-0000-0000-000000000001, 'Kouty nad Desnou', "
							"{ la: 50.1010566, lo: 17.1077972 }, ['Kouty', 'Loucna'], "
							"{ "
							"	{ "
							"		id: 00000000-0000-0000-0000-000000000001, "
							"		name: 'Chicken line', "
							"		segments_old: "
							"		{ "
							"			{ "
							"				id: 00000000-0000-0000-0000-000000000001, "
							"				name: 'First segment', "
							"				location_start: "
							"				{ "
							"					id: 00000000-0000-0000-0000-000000000001, "
							"					location: { la: 50.1010566, lo: 17.1077972 } "
							"				}, "
							"				location_stop: "
							"				{ "
							"					id: 00000000-0000-0000-0000-000000000002, "
							"					location: { la: 50.1010566, lo: 17.1077972 } "
							"				}, "
							"				valid_time_start: 1368438071000, "
							"				valid_time_stop: 1368438171000 "
							"			} "
							"		}, "
							"		segments_current: "
							"		[ "
							"			{ "
							"				id: 00000000-0000-0000-0000-000000000002, "
							"				name: 'Second segment', "
							"				location_start: "
							"				{ "
							"					id: 00000000-0000-0000-0000-000000000003, "
							"					location: { la: 50.1010566, lo: 17.1077972 } "
							"				}, "
							"				location_stop: "
							"				{ "
							"					id: 00000000-0000-0000-0000-000000000004, "
							"					location: { la: 50.1010566, lo: 17.1077972 } "
							"				}, "
							"				valid_time_start: 1368438071000, "
							"				valid_time_stop: 0 "
							"			} "
							"		], "
							"		valid_time_start: 1368438071000, "
							"		valid_time_stop: 1368438072000 "
							"	} "
							"}, "
							"{ "
							"	{ "
							"		id: 00000000-0000-0000-0000-000000000002, "
							"		name: 'Red track', "
							"		segments_old: {}, "
							"		segments_current: "
							"		[ "
							"			{ "
							"				id: 00000000-0000-0000-0000-000000000003, "
							"				name: 'Meadow', "
							"				location_start: "
							"				{ "
							"					id: 00000000-0000-0000-0000-000000000005, "
							"					location: { la: 50.1010566, lo: 17.1077972 } "
							"				}, "
							"				location_stop: "
							"				{ "
							"					id: 00000000-0000-0000-0000-000000000006, "
							"					location: { la: 50.1010566, lo: 17.1077972 } "
							"				}, "
							"				valid_time_start: 1368438071000, "
							"				valid_time_stop: 0 "
							"			}, "
							"			{ "
							"				id: 00000000-0000-0000-0000-000000000004, "
							"				name: 'Forest', "
							"				location_start: "
							"				{ "
							"					id: 00000000-0000-0000-0000-000000000007, "
							"					location: { la: 50.1010566, lo: 17.1077972 } "
							"				}, "
							"				location_stop: "
							"				{ "
							"					id: 00000000-0000-0000-0000-000000000008, "
							"					location: { la: 50.1010566, lo: 17.1077972 } "
							"				}, "
							"				valid_time_start: 1368438071000, "
							"				valid_time_stop: 0 "
							"			} "
							"		], "
							"		valid_time_start: 1368438071000, "
							"		valid_time_stop: 0 "
							"	} "
							"});")	
		p_echo_command = subprocess.Popen(['echo', add_spot_command], stdout=subprocess.PIPE)
		p_cqlsh = subprocess.Popen(self.cqlshCommand, stdin=p_echo_command.stdout, stdout=subprocess.PIPE)
		out, err = p_cqlsh.communicate()
		print "Db command 'add_spot_command' output: " + str(out)
		print "Db command 'add_spot_command' error output: " + str(err)
		'''
