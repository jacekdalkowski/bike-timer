USE biketimer;

CREATE TYPE geopoint(
	la double,
	lo double
);

CREATE TABLE spots (
	id int PRIMARY KEY,
	name text,
	position frozen<geopoint>,
	tags list<text>
);
	