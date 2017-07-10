# Biketimer web database

### Docker image source
https://hub.docker.com/_/cassandra/

### Run migration scripts inside container
```sh
docker exec -it biketimer-web-database /bin/bash
cd root/db_migrations/
python migrate.py [up|down|seed] [docker|local]
```

### Run cqlsh
```sh
docker run -it --link biketimer-web-database:cassandra --rm cassandra sh -c 'exec cqlsh "$CASSANDRA_PORT_9042_TCP_ADDR"'
```

```sh
desc keyspaces;
use biketimer;

desc tables;

select * from spots;
select * from users;
select * from runs_by_id;
```