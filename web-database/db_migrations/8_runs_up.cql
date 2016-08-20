USE biketimer;

CREATE TABLE runs_by_user_spot_date (
	id uuid,
	user_id uuid,
	spot_id uuid,
	time_start timestamp,
	run_info frozen<run_info>,
	PRIMARY KEY ((user_id, spot_id), time_start)
);

CREATE TABLE runs_by_user_date (
	id uuid,
	user_id uuid,
	time_start timestamp,
	run_info frozen<run_info>,
	PRIMARY KEY ((user_id), time_start)
);

CREATE TABLE runs_by_user_segment_date (
	id uuid,
	user_id uuid,
	segment_id uuid,
	time_start timestamp,
	run_info frozen<run_info>,
	PRIMARY KEY ((user_id, segment_id), time_start)
);

CREATE TABLE runs_by_spot_user_date (
	id uuid,
	spot_id uuid,
	user_id uuid,
	time_start timestamp,
	run_info frozen<run_info>,
	PRIMARY KEY ((spot_id), user_id, time_start)
);

CREATE TABLE runs_by_segment_date_time (
	id uuid,
	segment_id uuid,
	time_start timestamp,
	time_span_ms int,
	run_info frozen<run_info>,
	PRIMARY KEY ((segment_id), time_start, time_span_ms)
);

CREATE TABLE runs_by_segment_time (
	id uuid,
	segment_id uuid,
	time_span_ms int,
	time_start timestamp,
	run_info frozen<run_info>,
	PRIMARY KEY ((segment_id), time_span_ms)
);

CREATE TABLE runs_by_segment_user_date (
	id uuid,
	segment_id uuid,
	user_id uuid,
	time_start timestamp,
	run_info frozen<run_info>,
	PRIMARY KEY ((segment_id), user_id, time_start)
);

CREATE TABLE runs_by_id (
	id uuid,
	run_info frozen<run_info>,
	PRIMARY KEY (id)
);
