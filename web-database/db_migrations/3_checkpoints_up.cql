USE biketimer;

CREATE TYPE checkpoint (
	id uuid,
	location frozen<geopoint>
);

