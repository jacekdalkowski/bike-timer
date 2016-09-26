import os
from docker_digitalocean_common import *

def copy_webidentity_src_to_remote_host(ssh_con_str):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/../web-identity"
	print "Copying web-identity src (" + local_dir + ") to remote host."
	os.system("scp -r " + local_dir + " " + ssh_con_str + ":/root/apps/web-identity")
	print "Copying web-identity src to remote host finished."

def build_webidentity_continer_in_remote_host(ssh):
	print "Building biketimer/web-identity image in remote host."
	result = ssh("docker build -t biketimer/web-identity /root/apps/web-identity")
	print "Building biketimer/web-identity image in remote host result: "
	print result

def run_webidentity_container(ssh):
	print "Starting biketimer-web-identity container in remote host."
	result = ssh("docker run -p 8081:8081 --name biketimer-web-identity --link biketimer-web-database:cassandrahost -d biketimer/web-identity")
	print "Starting biketimer-web-identity container in remote host result: "
	print result

