USE biketimer;

CREATE TABLE runs_by_user_spot (
	id uuid,
	user_id uuid,
	spot_id uuid,
	run_info frozen<run_info>,
	PRIMARY KEY ((user_id), spot_id)
);

CREATE TABLE runs_by_user_segment (
	id uuid,
	user_id uuid,
	segment_id uuid,
	run_info frozen<run_info>,
	PRIMARY KEY ((user_id), segment_id)
);

CREATE TABLE runs_by_spot_user (
	id uuid,
	spot_id uuid,
	user_id uuid,
	run_info frozen<run_info>,
	PRIMARY KEY ((spot_id), user_id)
);

CREATE TABLE runs_by_segment_user (
	id uuid,
	segment_id uuid,
	user_id uuid,
	run_info frozen<run_info>,
	PRIMARY KEY ((segment_id), user_id)
);

