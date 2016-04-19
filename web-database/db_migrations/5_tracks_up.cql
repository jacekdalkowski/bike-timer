USE biketimer;

CREATE TYPE track (
	id uuid,
	name text,
	segments_old set<frozen<segment>>,
	segments_current list<frozen<segment>>,
	valid_time_start timestamp,
	valid_time_stop timestamp
);
