import subprocess
import re
import os
import time
import sh
import time
from docker_digitalocean_cassandra import *
from docker_digitalocean_webidentity import *
from docker_digitalocean_webapi import *

ssh_con_str = "root@46.101.148.70"

print "NOTICE: this script has to be run as a user with access to SSH keys."
print "Deployment to remote server (" + ssh_con_str + ") started."

ssh = sh.ssh.bake(ssh_con_str)

print "Successfully connected to remote server."

kill_and_remove_all_containers(ssh)

cassandra_container_id = start_cassandra_container(ssh)
print "Wait for cassandra to warm up."
time.sleep(20) # wait for cassandra to init.

print "Setup cassandra schema."
copy_cassandra_scripts_to_remote_host(cassandra_container_id, ssh_con_str)
copy_cassandra_scripts_to_docker_container(ssh, cassandra_container_id)
run_cassandra_migration_scripts_in_docker_container(ssh, cassandra_container_id)

print "Stop cassandra."
ssh("docker stop biketimer-web-database")

copy_webidentity_src_to_remote_host(ssh_con_str)
build_webidentity_continer_in_remote_host(ssh)

copy_webapi_src_to_remote_host(ssh_con_str)
build_webapi_continer_in_remote_host(ssh)

print "Start cassandra."
ssh("docker start biketimer-web-database")
print "Wait for cassandra to warm up."
time.sleep(20)

print "Start webapi."
run_webapi_container(ssh)

print "Start webidentity."
run_webidentity_container(ssh)



