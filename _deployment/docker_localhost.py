import subprocess
import re

def run_command(command_and_args):
    p = subprocess.Popen(command_and_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out

def kill_and_remove_all_containers():
    p = subprocess.Popen(['docker', 'ps', '-a', '-q'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    for container_info in out.split('\n'):
        run_command(['docker', 'kill', container_info])
        run_command(['docker', 'rm', container_info])


kill_and_remove_all_containers()

# Check if docker machine works
docker_machine_name = 'default'
default_machine_status = run_command(['docker-machine', 'status', docker_machine_name])
default_machine_status = default_machine_status.strip()
print 'Status of docker machine: ' + docker_machine_name + ' is: ' + default_machine_status + '.'

if default_machine_status.lower() == 'running':
    print 'Machine already running. Proceeding.'
elif default_machine_status.lower() == 'stopped' or default_machine_status.lower() == 'saved':
    print 'Attemting to run docker machine: ' + docker_machine_name
    run_command(['docker-machine', 'start', 'default'])
    default_machine_status = run_command(['docker-machine', 'status', docker_machine_name])
    default_machine_status = default_machine_status.strip()
    print 'Status of docker machine: ' + docker_machine_name + ' is: ' + default_machine_status + '.'
    if default_machine_status.lower() != 'running':
        print 'Could not start docker machine: ' + docker_machine_name + '. Exiting.'

#print 'Executing \'eval "$(docker-machine env default)"\' command.'
#a = run_command(['docker-machine', 'env', docker_machine_name])
#print a
#run_command(['eval', '$(' + a + ')'])

#docker_machine_variables = run_command(['docker-machine', 'env', docker_machine_name])
#for docker_machine_variable in docker_machine_variables.split('\n'):
#   print 'Executing: \'' + docker_machine_variable + '\'.'
#   print docker_machine_variable.split(' ')
#   run_command(docker_machine_variable.split(' '))

docker_running_containers_info = run_command(['docker', 'ps']).split('\n')
docker_running_containers_info.remove('')
cassandra_container_running = False
for docker_running_container_info in docker_running_containers_info:
    if re.split('\\s+', docker_running_container_info)[1] == 'cassandra':
        cassandra_container_running = True;

if cassandra_container_running:
    print 'Cassandra container running. Proceeding.'
else:
    print 'Starting Cassandra container.'
    starting_cassandra_result = run_command(['docker', 'run', '--name', 'bt-database', '-d', 'cassandra']).split('\n')
    starting_cassandra_result.remove('')
    print 'Starting cassandra result: ' + starting_cassandra_result[-1]

print 'Building jd/bt-identity container.'
building_btidentity_result = run_command(['docker', 'build', '-t', 'jd/bt-identity', '../web-identity']).split('\n')
building_btidentity_result.remove('')
building_btidentity_result = building_btidentity_result[-1]
print 'Building jd/bt-identity container result: ' + building_btidentity_result
if re.match('^Successfully', building_btidentity_result):
    print 'Building jd/bt-identity container successful. Proceeding.'
else:
    print 'Building jd/bt-identity container failed.'
    exit()

print 'Starting jd/bt-identity container.'
starting_btidentity_result = run_command(['docker', 'run', '--name', 'bt-identity', '-P', '--link', 'bt-database:cassandrahost', '-d', 'jd/bt-identity']).split('\n')
print starting_btidentity_result
starting_btidentity_result.remove('')
starting_btidentity_result = starting_btidentity_result[-1]
print 'Starting jd/bt-identity container result: ' + starting_btidentity_result

#docker_images_info = run_command(['docker', 'images']).split('\n')
#for docker_image_info in docker_images_info:
#   if re.split('\s+', docker_image_info)[0] == 'cassandra':
#       print docker_image_info

