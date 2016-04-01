USE biketimer;

CREATE TABLE users (
    id uuid,
    fb_id text,
    bt_name text,
    email text,
    fb_access_token text,
    fb_name text,
    fb_surname text,
    roles list<text>,
    friends_ids list<uuid>,
    PRIMARY KEY (id)
);

create index on users(fb_id);
