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
        return Deployment(apiEndpoint, identityEndpoint)

