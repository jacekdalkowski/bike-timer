import subprocess
import re
from deployment import Deployment
from endpoint import Endpoint 

class LocalDeployment:

    @staticmethod
    def run_command(command_and_args):
        p = subprocess.Popen(command_and_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out

    @staticmethod
    def GetEndpoint(container_name):
    	# docker ps --format {{.Names}}\t{{.Ports}}
        containers_and_ports = LocalDeployment.run_command(['docker', 'ps', '--format', '{{.Names}}\t{{.Ports}}']).split('\n')
        for container_and_ports in containers_and_ports:
            container = container_and_ports.split('\t')[0]
            if container == container_name:
                ports = container_and_ports.split('\t')[1]
                port = re.match('(.*:)(\\d+)', ports).groups()[1]
                return Endpoint('192.168.99.100', port)
        raise Exception('No container: ' + container_name + ' found.')

    @staticmethod
    def GetLocalDockerDeployment():
        apiEndpoint = LocalDeployment.GetEndpoint('biketimer_web-api')
        identityEndpoint = LocalDeployment.GetEndpoint('biketimer_web-identity')
        return Deployment(apiEndpoint, identityEndpoint, RunCqlOnLocalDockerDeployment)

    @staticmethod
    def RunCqlOnLocalDockerDeployment(cmd):
        p_echo_command = subprocess.Popen(['echo', cmd], stdout=subprocess.PIPE)
        cqlshCommand = ['docker', 'run', '-i', '--link', 'biketimer_web-database:cassandra', '--rm', 'cassandra:3.0.0', 'cqlsh', 'cassandra']
        p_cqlsh = subprocess.Popen(cqlshCommand, stdin=p_echo_command.stdout, stdout=subprocess.PIPE)
        out, err = p_cqlsh.communicate()

    @staticmethod
    def GetLocalDeployment():
        apiEndpoint = Endpoint('localhost', '5001')
        identityEndpoint = Endpoint('localhost', '8081')
        return Deployment(apiEndpoint, identityEndpoint, RunCqlOnLocalDeployment)

    @staticmethod
    def RunCqlOnLocalDeployment(cmd):
        p_echo_command = subprocess.Popen(['echo', cmd], stdout=subprocess.PIPE)
        cqlshCommand = ['/Users/jacekdalkowski/Dev/_cassandra/apache-cassandra-3.0.0/bin/cqlsh']
        p_cqlsh = subprocess.Popen(cqlshCommand, stdin=p_echo_command.stdout, stdout=subprocess.PIPE)
        out, err = p_cqlsh.communicate()


