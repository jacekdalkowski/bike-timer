from docker_digitalocean_common import *

def copy_webapi_src_to_remote_host(ssh_con_str):
	pwd = run_local_command("pwd").rstrip()
	local_dir = pwd + "/../web-api"
	print "Copying web-api src (" + local_dir + ") to remote host."
	os.system("scp -r " + local_dir + " " + ssh_con_str + ":/root/apps/web-api")
	print "Copying web-api src to remote host finished."

def build_webapi_continer_in_remote_host(ssh):
	print "Building biketimer/web-api image in remote host."
	result = ssh("docker build -t biketimer/web-api /root/apps/web-api")
	print "Building biketimer/web-api image in remote host result: "
	print result

def run_webapi_container(ssh):
	print "Starting biketimer-web-api container in remote host."
	result = ssh("docker run -p 5001:5001 --name biketimer-web-api -P --link biketimer-web-database:cassandrahost -d biketimer/web-api")
	print "Starting biketimer-web-api container in remote host result: "
	print result

