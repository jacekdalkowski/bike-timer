import subprocess
import re
import os
import time
import sh
from docker_digitalocean_common import *

def start_cassandra_container(ssh):
    print "Starting cassandra container."
    result = ssh("docker run --name biketimer-web-database -d cassandra:3.0")
    print "Starting cassandra container result:"
    print result
    return str(result).rstrip()

def copy_cassandra_scripts_to_remote_host(cassandra_container_id, ssh_con_str):
    print "Copying cassandra scripts to remote host."
    pwd = run_local_command("pwd").rstrip()
    print "pwd: " + pwd
    local_dir = pwd + "/../web-database/db_migrations"
    print "local dir to copy: " + local_dir
    os.system("scp -r " + local_dir + " " + ssh_con_str + ":/root")
    print "Cassandra scripts copied to remote host."

def copy_cassandra_scripts_to_docker_container(ssh, container_id):
    print "Copying cassandra scripts to docker container."
    result = ssh("docker cp /root/db_migrations/ " + container_id + ":/root/db_migrations")
    print "Copying cassandra scripts to docker container result:"
    print result

def run_cassandra_migration_scripts_in_docker_container(ssh, container_id):
    print "Running cassandra migration DOWN scripts in docker container."
    result = ssh("docker exec " + container_id + " python /root/db_migrations/migrate.py down docker")
    print "Migration scripts result:"
    print result

    print "Running cassandra migration UP scripts in docker container."
    result = ssh("docker exec " + container_id + " python /root/db_migrations/migrate.py up docker")
    print "Migration scripts result:"
    print result


