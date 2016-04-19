USE biketimer;

ALTER TABLE spots ADD tracks_old set<frozen<track>>;
ALTER TABLE spots ADD tracks_current set<frozen<track>>;
