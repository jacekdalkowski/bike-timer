USE biketimer;

CREATE TYPE segment (
	id uuid,
	name text,
	location_start frozen<checkpoint>,
	location_stop frozen<checkpoint>,
	valid_time_start timestamp,
	valid_time_stop timestamp
);
