USE biketimer;

CREATE TYPE geopoint(
	la double,
	lo double
);

CREATE TABLE spots (
	id uuid PRIMARY KEY,
	name text,
	position frozen<geopoint>,
	tags list<text>
);
	