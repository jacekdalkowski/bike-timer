USE biketimer;

UPDATE spots
set tracks_old = { 
	{
		id: 00000000-0000-0000-0000-000000000001,
		name: 'Chicken line',
		segments_old: 
		{
			{
				id: 00000000-0000-0000-0000-000000000001,
				name: 'First segment',
				location_start:
				{
					id: 00000000-0000-0000-0000-000000000001,
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				location_stop:
				{
					id: 00000000-0000-0000-0000-000000000002,
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				valid_time_start: '2011-02-03T04:05+0000',
				valid_time_stop: '2012-02-03T04:05+0000'
			}
		},
		segments_current:
		[
			{
				id: 00000000-0000-0000-0000-000000000002,
				name: 'Second segment',
				location_start:
				{
					id: 00000000-0000-0000-0000-000000000003,
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				location_stop:
				{
					id: 00000000-0000-0000-0000-000000000004,
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				valid_time_start: '2015-02-03T04:05+0000',
				valid_time_stop: 0
			}
		],
		valid_time_start: '2013-02-03T04:05+0000',
		valid_time_stop: '2014-02-03T04:05+0000'
	} 
},
tracks_current = {
	{
		id: 00000000-0000-0000-0000-000000000002,
		name: 'Red track',
		segments_old: {},
		segments_current:
		[
			{
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
				valid_time_start: '2015-02-03T04:05+0000',
				valid_time_stop: 0
			},
			{
				id: 00000000-0000-0000-0000-000000000004,
				name: 'Forest',
				location_start:
				{
					id: 00000000-0000-0000-0000-000000000007,
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				location_stop:
				{
					id: 00000000-0000-0000-0000-000000000008,
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				valid_time_start: '2015-02-03T04:05+0000',
				valid_time_stop: 0
			}
		],
		valid_time_start: '2015-02-03T04:05+0000',
		valid_time_stop: 0
	} 
}
where id = 00000000-0000-0000-0000-000000000001;

