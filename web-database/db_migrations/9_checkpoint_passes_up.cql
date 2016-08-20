USE biketimer;

CREATE TABLE checkpoint_passes_by_user_time (
	id uuid,
	user_id uuid,
	time timestamp,
	checkpoint frozen<checkpoint>,
	PRIMARY KEY ((user_id), time, id)
);

CREATE TABLE checkpoint_passes_by_user_id (
	id uuid,
	user_id uuid,
	time timestamp,
	checkpoint frozen<checkpoint>,
	PRIMARY KEY ((user_id), id, time)
);