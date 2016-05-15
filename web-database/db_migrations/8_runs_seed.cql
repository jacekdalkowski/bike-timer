USE biketimer;

INSERT INTO runs_by_user_spot_date(id, user_id, spot_id, time_start, run_info)
VALUES (00000000-0000-0000-0000-000000000001, 
	00000000-0000-0000-0000-000000000001, 
	00000000-0000-0000-0000-000000000001,
	1461528287000,
	{
		id: 00000000-0000-0000-0000-000000000001,
		user_id: 00000000-0000-0000-0000-000000000001,
		user_bt_name: 'Jacek Dalkowski',
		segment: {
			id: 00000000-0000-0000-0000-000000000003,
			name: 'Meadow',
			location_start:
			{
				id: 00000000-0000-0000-0000-000000000005,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			location_stop:
			{
				id: 00000000-0000-0000-0000-000000000006,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			valid_time_start: 1368438071000,
			valid_time_stop: 0
		},
		time_start: 1461528287000,
		time_stop: 1461528887000,
		time_span_ms: 600000
	});

INSERT INTO runs_by_user_date(id, user_id, time_start, run_info)
VALUES (00000000-0000-0000-0000-000000000001, 
	00000000-0000-0000-0000-000000000001,
	1461528287000,
	{
		id: 00000000-0000-0000-0000-000000000001,
		user_id: 00000000-0000-0000-0000-000000000001,
		user_bt_name: 'Jacek Dalkowski',
		segment: {
			id: 00000000-0000-0000-0000-000000000003,
			name: 'Meadow',
			location_start:
			{
				id: 00000000-0000-0000-0000-000000000005,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			location_stop:
			{
				id: 00000000-0000-0000-0000-000000000006,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			valid_time_start: 1368438071000,
			valid_time_stop: 0
		},
		time_start: 1461528287000,
		time_stop: 1461528887000,
		time_span_ms: 600000
	});

INSERT INTO runs_by_user_segment_date(id, user_id, segment_id, time_start, run_info)
VALUES (00000000-0000-0000-0000-000000000001, 
	00000000-0000-0000-0000-000000000001, 
	00000000-0000-0000-0000-000000000003,
	1461528287000,
	{
		id: 00000000-0000-0000-0000-000000000001,
		user_id: 00000000-0000-0000-0000-000000000001,
		user_bt_name: 'Jacek Dalkowski',
		segment: {
			id: 00000000-0000-0000-0000-000000000003,
			name: 'Meadow',
			location_start:
			{
				id: 00000000-0000-0000-0000-000000000005,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			location_stop:
			{
				id: 00000000-0000-0000-0000-000000000006,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			valid_time_start: 1368438071000,
			valid_time_stop: 0
		},
		time_start: 1461528287000,
		time_stop: 1461528887000,
		time_span_ms: 600000
	});

INSERT INTO runs_by_spot_user_date(id, spot_id, user_id, time_start, run_info)
VALUES (00000000-0000-0000-0000-000000000001, 
	00000000-0000-0000-0000-000000000001, 
	00000000-0000-0000-0000-000000000001,
	1461528287000,
	{
		id: 00000000-0000-0000-0000-000000000001,
		user_id: 00000000-0000-0000-0000-000000000001,
		user_bt_name: 'Jacek Dalkowski',
		segment: {
			id: 00000000-0000-0000-0000-000000000003,
			name: 'Meadow',
			location_start:
			{
				id: 00000000-0000-0000-0000-000000000005,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			location_stop:
			{
				id: 00000000-0000-0000-0000-000000000006,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			valid_time_start: 1368438071000,
			valid_time_stop: 0
		},
		time_start: 1461528287000,
		time_stop: 1461528887000,
		time_span_ms: 600000
	});

INSERT INTO runs_by_segment_date_time(id, segment_id, time_start, time_span_ms, run_info)
VALUES(00000000-0000-0000-0000-000000000001, 
	00000000-0000-0000-0000-000000000003,
	1461528287000,
	600000,
	{
		id: 00000000-0000-0000-0000-000000000001,
		user_id: 00000000-0000-0000-0000-000000000001,
		user_bt_name: 'Jacek Dalkowski',
		segment: {
			id: 00000000-0000-0000-0000-000000000003,
			name: 'Meadow',
			location_start:
			{
				id: 00000000-0000-0000-0000-000000000005,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			location_stop:
			{
				id: 00000000-0000-0000-0000-000000000006,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			valid_time_start: 1368438071000,
			valid_time_stop: 0
		},
		time_start: 1461528287000,
		time_stop: 1461528887000,
		time_span_ms: 600000
	});

INSERT INTO runs_by_segment_user_date(id, segment_id, user_id, time_start, run_info)
VALUES (00000000-0000-0000-0000-000000000001, 
	00000000-0000-0000-0000-000000000003, 
	00000000-0000-0000-0000-000000000001,
	1461528287000,
	{
		id: 00000000-0000-0000-0000-000000000001,
		user_id: 00000000-0000-0000-0000-000000000001,
		user_bt_name: 'Jacek Dalkowski',
		segment: {
			id: 00000000-0000-0000-0000-000000000003,
			name: 'Meadow',
			location_start:
			{
				id: 00000000-0000-0000-0000-000000000005,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			location_stop:
			{
				id: 00000000-0000-0000-0000-000000000006,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			valid_time_start: 1368438071000,
			valid_time_stop: 0
		},
		time_start: 1461528287000,
		time_stop: 1461528887000,
		time_span_ms: 600000
	});

INSERT INTO runs_by_id(id, run_info)
VALUES (00000000-0000-0000-0000-000000000001, 
	{
		id: 00000000-0000-0000-0000-000000000001,
		user_id: 00000000-0000-0000-0000-000000000001,
		user_bt_name: 'Jacek Dalkowski',
		segment: {
			id: 00000000-0000-0000-0000-000000000003,
			name: 'Meadow',
			location_start:
			{
				id: 00000000-0000-0000-0000-000000000005,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			location_stop:
			{
				id: 00000000-0000-0000-0000-000000000006,
				location: { la: 50.1010566, lo: 17.1077972 }
			},
			valid_time_start: 1368438071000,
			valid_time_stop: 0
		},
		time_start: 1461528287000,
		time_stop: 1461528887000,
		time_span_ms: 600000
	});
