import sys
import os
import re
from subprocess import call
from operator import itemgetter, attrgetter, methodcaller

CASSANDRA_PATH = '/Users/jacekdalkowski/Dev/_cassandra/apache-cassandra-2.2.3'
ARTIFACTS_PATH = '/Users/jacekdalkowski/Dev/bike_timer/web-api/biketimerwebapi/_artifacts'

def filename_prefix_to_int(file_name):
	p = re.compile("(\d+).*")
	m = p.search(file_name)
	if m:
		return int(m.group(1))
	else:
		return None

def db_operation(current_dir, file_sufix, reverse):
	files = []
	for file in os.listdir(current_dir):
		if file.endswith(file_sufix):
			files += [file]
	prefix_and_files = map(lambda f: { 'id': filename_prefix_to_int(f), 'file': f}, files)
	int_prefix_and_files = filter(lambda pf: pf['id'], prefix_and_files)
	sorted_int_prefix_and_files = sorted(int_prefix_and_files, key=lambda d: d['id'], reverse=reverse)
	print sorted_int_prefix_and_files
	for file in sorted_int_prefix_and_files:
		call([CASSANDRA_PATH + '/bin/cqlsh', '-e', 'SOURCE \'' + ARTIFACTS_PATH + '/db_migrations/' + file['file'] + '\''])


current_dir = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) < 2:
	print 'A paramter is required: up, down or seed.'
elif sys.argv[1] == 'up':
	db_operation(current_dir, "_up.cql", False)
elif sys.argv[1] == 'down':
	db_operation(current_dir, "_down.cql", True)
elif sys.argv[1] == 'seed':
	db_operation(current_dir, "_seed.cql", False)
else:
	print 'Available commands are: up, down and seed.'
