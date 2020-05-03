import socket

HOST = 'www.google.com'
PORT = 80
DATA = 'GET / HTTP/1.0\r\nHost: google.com\r\n\r\n'

def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(DATA.encode('utf-8'))
    response = client.recv(4096)
    return response.decode('utf-8')
    
if __name__ == '__main__':
    print(tcp_client())