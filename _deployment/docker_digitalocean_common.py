import subprocess
import re
import os
import time
import sh

def run_local_command(command_and_args):
    p = subprocess.Popen(command_and_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out

def kill_and_remove_all_containers(ssh):
    # docker ps -a -q
    running_containers = ssh('docker ps -q')
    print 'running_containers: ' + str(running_containers)
    if running_containers:
        for running_container_info in running_containers.split('\n'):
            if running_container_info:
                print 'killing docker container: ' + running_container_info
                ssh('docker kill ' + running_container_info)
    all_containers = ssh('docker ps -a -q')
    if all_containers:
        for container_info in all_containers.split('\n'):
            if container_info:
                print 'removing docker container: ' + container_info
                ssh('docker rm ' + container_info)



