import subprocess
import re
import os
import time

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

def run_docker_machine():
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

def run_cassandra_container():
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

def filename_prefix_to_int(file_name):
    p = re.compile("(\d+).*")
    m = p.search(file_name)
    if m:
        return int(m.group(1))
    else:
        return None

def setup_database_schema():
    files = []
    for file in os.listdir('../web-database/db_migrations'):
        if file.endswith('_up.cql'):
            files += [file]
    prefix_and_files = map(lambda f: { 'id': filename_prefix_to_int(f), 'file': f}, files)
    sorted_int_prefix_and_files = sorted(prefix_and_files, key=lambda d: d['id'])
    for file in sorted_int_prefix_and_files:
        p_cat = subprocess.Popen(['cat', '../web-database/db_migrations/' + file['file']], stdout=subprocess.PIPE)
        p_docker = subprocess.Popen(['docker', 'run', '-i', '--link', 'bt-database:cassandra', '--rm', 'cassandra', 'cqlsh', 'cassandra'], stdin=p_cat.stdout, stdout=subprocess.PIPE)
        out, err = p_docker.communicate()
        print out

def build_identity_container():
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

def run_identity_container():
    print 'Starting jd/bt-identity container.'
    starting_btidentity_result = run_command(['docker', 'run', '--name', 'bt-identity', '-P', '--link', 'bt-database:cassandrahost', '-d', 'jd/bt-identity']).split('\n')
    print starting_btidentity_result
    starting_btidentity_result.remove('')
    starting_btidentity_result = starting_btidentity_result[-1]
    print 'Starting jd/bt-identity container result: ' + starting_btidentity_result

kill_and_remove_all_containers()

run_docker_machine()
run_cassandra_container()
time.sleep(20)
setup_database_schema()

build_identity_container()
run_identity_container()


