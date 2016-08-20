USE biketimer;

CREATE TABLE checkpoint_passes (
	id uuid,
	user_id uuid,
	time timestamp,
	checkpoint frozen<checkpoint>,
	PRIMARY KEY ((user_id), time, id)
);