import sshtunnel
from getpass import getpass

ssh_host = 'localhost'
ssh_port = 22
ssh_user = 'n3'

REMOTE_HOST = 'localhost'
REMOTE_PORT = 21

from sshtunnel import SSHTunnelForwarder
ssh_password = getpass('Enter YOUR SSH PASSWORD: ')

server = SSHTunnelForwarder(
    ssh_address=(ssh_host, ssh_port),
    ssh_username=ssh_user,
    ssh_password=ssh_password,
    remote_bind_address=(REMOTE_HOST, REMOTE_PORT))
    
server.start()

print('Connect the remote service via local port: %s' %server.local_bind_port)

try:
    while True:
        pass
except KeyboardInterrupt:
    print('Exiting user user request.:\n')
    server.stop()