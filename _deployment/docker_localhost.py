import subprocess
import re
import os
import time

def run_command(command_and_args):
    p = subprocess.Popen(command_and_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out

def kill_and_remove_all_containers():
    # docker ps -a -q
    containers = run_command(['docker', 'ps', '-a', '-q'])
    for container_info in containers.split('\n'):
        run_command(['docker', 'kill', container_info])
        run_command(['docker', 'rm', container_info])

def run_docker_machine():
    docker_machine_name = 'default'
    # docker-machine status default
    default_machine_status = run_command(['docker-machine', 'status', docker_machine_name])
    default_machine_status = default_machine_status.strip()
    print 'Status of docker machine: ' + docker_machine_name + ' is: ' + default_machine_status + '.'

    if default_machine_status.lower() == 'running':
        print 'Machine already running. Proceeding.'
    elif default_machine_status.lower() == 'stopped' or default_machine_status.lower() == 'saved':
        print 'Attemting to run docker machine: ' + docker_machine_name
        # docker-machine start default
        run_command(['docker-machine', 'start', 'default'])
        # docker-machine status default
        default_machine_status = run_command(['docker-machine', 'status', docker_machine_name])
        default_machine_status = default_machine_status.strip()
        print 'Status of docker machine: ' + docker_machine_name + ' is: ' + default_machine_status + '.'
        if default_machine_status.lower() != 'running':
            print 'Could not start docker machine: ' + docker_machine_name + '. Exiting.'

def run_cassandra_container():
    # docker ps
    docker_running_containers_info = run_command(['docker', 'ps']).split('\n')
    docker_running_containers_info.remove('')
    cassandra_container_running = False
    for docker_running_container_info in docker_running_containers_info:
        if re.split('\\s+', docker_running_container_info)[1] == 'cassandra:2.2.5':
            cassandra_container_running = True;

    if cassandra_container_running:
        print 'Cassandra container running. Proceeding.'
    else:
        print 'Starting Cassandra container.'
        # docker run --name biketimer_web-database -d cassandra:2.2.5
        starting_cassandra_result = run_command(['docker', 'run', '--name', 'biketimer_web-database', '-d', 'cassandra:2.2.5']).split('\n')
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
        p_docker = subprocess.Popen(['docker', 'run', '-i', '--link', 'biketimer_web-database:cassandra', '--rm', 'cassandra:2.2.5', 'cqlsh', 'cassandra'], stdin=p_cat.stdout, stdout=subprocess.PIPE)
        out, err = p_docker.communicate()
        print out

def build_identity_container():
    print 'Building biketimer/web-identity container.'
    # docker build -t biketimer/web-identity ../web-identity
    building_btidentity_result = run_command(['docker', 'build', '-t', 'biketimer/web-identity', '../web-identity']).split('\n')
    building_btidentity_result.remove('')
    building_btidentity_result = building_btidentity_result[-1]
    print 'Building biketimer/web-identity container result: ' + building_btidentity_result
    if re.match('^Successfully', building_btidentity_result):
        print 'Building biketimer/web-identity container successful. Proceeding.'
    else:
        print 'Building biketimer/web-identity container failed.'
        exit()

def run_identity_container():
    print 'Starting biketimer/web-identity container.'
    # docker run --name biketimer_web-identity -P --link biketimer_web-database:cassandrahost -d biketimer/web-identity
    starting_btidentity_result = run_command(['docker', 'run', '--name', 'biketimer_web-identity', '-P', '--link', 'biketimer_web-database:cassandrahost', '-d', 'biketimer/web-identity']).split('\n')
    print starting_btidentity_result
    starting_btidentity_result.remove('')
    starting_btidentity_result = starting_btidentity_result[-1]
    print 'Starting biketimer/web-identity container result: ' + starting_btidentity_result

def build_webapi_container():
    print 'Building biketimer/web-api container.'
    # docker build -t biketimer/web-api ../web-api
    building_webapi_result = run_command(['docker', 'build', '-t', 'biketimer/web-api', '../web-api']).split('\n')
    building_webapi_result.remove('')
    building_webapi_result = building_webapi_result[-1]
    print 'Building biketimer/web-api container result: ' + building_webapi_result
    if re.match('^Successfully', building_webapi_result):
        print 'Building biketimer/web-api container successful. Proceeding.'
    else:
        print 'Building biketimer/web-api container failed.'
        exit()

def run_webapi_container():
    print 'Starting biketimer/web-api container.'
    # docker run --name biketimer_web-api -P --link biketimer_web-database:cassandrahost -d biketimer/web-api
    starting_webapi_result = run_command(['docker', 'run', '--name', 'biketimer_web-api', '-P', '--link', 'biketimer_web-database:cassandrahost', '-d', 'biketimer/web-api']).split('\n')
    print starting_webapi_result
    starting_webapi_result.remove('')
    starting_webapi_result = starting_webapi_result[-1]
    print 'Starting biketimer/web-api container result: ' + starting_webapi_result

kill_and_remove_all_containers()

run_docker_machine()
run_cassandra_container()
time.sleep(20) # wait for cassandra to init.
setup_database_schema()

build_identity_container()
run_identity_container()

build_webapi_container()
run_webapi_container()


