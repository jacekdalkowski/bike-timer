
# migrate.py [up|seed|down] [local|docker]
# e.g. migrate.py up docker

import sys
import os
import re
from subprocess import call, check_output
from operator import itemgetter, attrgetter, methodcaller

CASSANDRA_PATH_LOCAL = '/Users/jacekdalkowski/Dev/_cassandra/apache-cassandra-3.0.0/bin/'
ARTIFACTS_PATH_LOCAL = '/Users/jacekdalkowski/Dev/bike_timer/web-database/db_migrations'

CASSANDRA_PATH_DOCKER = ''
ARTIFACTS_PATH_DOCKER = '/root/db_migrations'

def filename_prefix_to_int(file_name):
	p = re.compile("(\d+).*")
	m = p.search(file_name)
	if m:
		return int(m.group(1))
	else:
		return None

def db_operation(current_dir, file_sufix, env, reverse):

	cassandra_path = None;
	artifacts_path = None;

	if env == 'local':
		cassandra_path = CASSANDRA_PATH_LOCAL
		artifacts_path = ARTIFACTS_PATH_LOCAL
	elif env == 'docker':
		cassandra_path = CASSANDRA_PATH_DOCKER
		artifacts_path = ARTIFACTS_PATH_DOCKER


	files = []
	for file in os.listdir(current_dir):
		if file.endswith(file_sufix):
			files += [file]
	prefix_and_files = map(lambda f: { 'id': filename_prefix_to_int(f), 'file': f}, files)
	#int_prefix_and_files = filter(lambda pf: pf['id'], prefix_and_files)
	sorted_int_prefix_and_files = sorted(prefix_and_files, key=lambda d: d['id'], reverse=reverse)
	print sorted_int_prefix_and_files
	for file in sorted_int_prefix_and_files:
		cqlsh_path = cassandra_path + 'cqlsh'
		source_arg = 'SOURCE \'' + artifacts_path + '/' + file['file'] + '\''
		call_args = [cqlsh_path, '-e', source_arg]
		print call_args
		call_output = check_output(call_args)
		print call_output


current_dir = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) < 3:
	print 'A parameter is required: up, down or seed.'
	print 'A parameter is required: local or docker.'
	quit()

env = None
if sys.argv[2] == 'local':
	env = 'local'
elif sys.argv[2] == 'docker':
	env = 'docker'
else:
	print 'Available envs are: local and docker.'


if sys.argv[1] == 'up':
	db_operation(current_dir, "_up.cql", env, False)
elif sys.argv[1] == 'down':
	db_operation(current_dir, "_down.cql", env, True)
elif sys.argv[1] == 'seed':
	db_operation(current_dir, "_seed.cql", env, False)
else:
	print 'Available commands are: up, down and seed.'
