USE biketimer;

CREATE TYPE run_info (
	id uuid,
	user_id uuid,
	user_bt_name text,
	segment frozen<segment>,
	time_start timestamp,
	time_stop timestamp,
	time_span_ms int
);
