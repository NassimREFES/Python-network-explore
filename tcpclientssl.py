import socket
import ssl
from ssl import wrap_socket, CERT_NONE, PROTOCOL_TLSv1, SSLError
from ssl import SSLContext
from ssl import HAS_SNI
from pprint import pprint

TARGET_HOST = 'www.google.com'
SSL_PORT = 443

# certificate authority certificate path
CA_CERT_PATH = '/usr/local/lib/python3.5/dist-packages/certifi/cacert.pem'

def ssl_wrap_socket(sock, keyfile=None, certfile=None, 
    cert_reqs=None, ca_certs=None, server_hostname=None, 
    ssl_version=None):
    context = SSLContext(ssl_version)
    context.verify_mode = cert_reqs
    
    if ca_certs:
        try:
            context.load_verify_locations(ca_certs)
            print('------')
        except Exception as e:
            raise SSLError(e)
    else:
        context.load_default_certs(purpose=Purpose.SERVER_AUTH)
    
    if certfile:
        context.load_cert_chain(certfile, keyfile)
     
    if HAS_SNI: # server name indication enabled by OpenSSL
        return context.wrap_socket(sock, server_hostname=server_hostname)
        
    return context.wrap_socket(sock)
    
if __name__ == '__main__':
    hostname = input('Enter target host: ') or TARGET_HOST
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((hostname, 443))
    
    ssl_socket = ssl_wrap_socket(client_sock,
    ssl_version=PROTOCOL_TLSv1,
    cert_reqs=ssl.CERT_REQUIRED,
    ca_certs=CA_CERT_PATH,
    server_hostname=hostname)
    
    print('Extracting remote host certificate details: ')
    
    cert = ssl_socket.getpeercert()
    pprint(cert)
    if not cert or ('commonName', TARGET_HOST) not in cert['subject'][4]:
        raise Exception('Invalid ssl cert for host %s, check if this is a man in the middle attack' % hostname)
        
    ssl_socket.write('GET / \n'.encode('utf-8'))
    #pprint(ssl_socket.recv(1024).split(b'\r\n'))
    ssl_socket.close()
    client_sock.close()
    
    
