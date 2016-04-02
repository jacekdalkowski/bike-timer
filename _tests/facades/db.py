import subprocess

class DbFacade:

	def clear_tables(self):
		delete_from_tables_command = 'use biketimer; truncate users;'
		p_echo_command = subprocess.Popen(['echo', delete_from_tables_command], stdout=subprocess.PIPE)
		p_docker = subprocess.Popen(['docker', 'run', '-i', '--link', 'biketimer_web-database:cassandra', '--rm', 'cassandra:2.2.5', 'cqlsh', 'cassandra'], stdin=p_echo_command.stdout, stdout=subprocess.PIPE)
		out, err = p_docker.communicate()
		print "Db command " + str(delete_from_tables_command) + " output: " + str(out)
		print "Db command " + str(delete_from_tables_command) + " error output: " + str(err)
