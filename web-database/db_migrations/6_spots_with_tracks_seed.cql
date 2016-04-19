USE biketimer;

UPDATE spots
set tracks_old = { 
	{
		id: now(),
		name: 'Chicken line',
		segments_old: 
		{
			{
				id: now(),
				name: 'First segment',
				location_start:
				{
					id: now(),
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				location_stop:
				{
					id: now(),
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				valid_time_start: 1368438071000,
				valid_time_stop: 1368438171000
			}
		},
		segments_current:
		[
			{
				id: now(),
				name: 'Second segment',
				location_start:
				{
					id: now(),
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				location_stop:
				{
					id: now(),
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				valid_time_start: 1368438071000,
				valid_time_stop: 0
			}
		],
		valid_time_start: 1368438071000,
		valid_time_stop: 1368438072000
	} 
},
tracks_current = {
	{
		id: now(),
		name: 'Red track',
		segments_old: {},
		segments_current:
		[
			{
				id: now(),
				name: 'Meadow',
				location_start:
				{
					id: now(),
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				location_stop:
				{
					id: now(),
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				valid_time_start: 1368438071000,
				valid_time_stop: 0
			},
			{
				id: now(),
				name: 'Forest',
				location_start:
				{
					id: now(),
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				location_stop:
				{
					id: now(),
					location: { la: 50.1010566, lo: 17.1077972 }
				},
				valid_time_start: 1368438071000,
				valid_time_stop: 0
			}
		],
		valid_time_start: 1368438071000,
		valid_time_stop: 0
	} 
}
where id = f3856552-65f8-8738-e0a6-4e99759cea06