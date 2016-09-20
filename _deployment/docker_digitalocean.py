import subprocess
import re
import os
import time
import sh
from docker_digitalocean_cassandra import *

ssh_con_str = "root@46.101.148.70"

print "NOTICE: this script has to be run as a user with access to SSH keys."
print "Deployment to remote server (" + ssh_con_str + ") started."

ssh = sh.ssh.bake(ssh_con_str)

print "Successfully connected to remote server."

kill_and_remove_all_containers(ssh)
setup_cassandra(ssh)


