import socket
from time import ctime

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(0)
    sock.settimeout(None)
    sock.bind(('127.0.0.1', 555))
    
    socket_address = sock.getsockname()
    
    print('Asynchronous socket server launched on socket: %s' % str(socket_address))
    
    while 1:
        sock.listen(1)
        sock.settimeout(5)
        print('------')
        client_sock, addr = sock.accept()
        data = client_sock.recv(4096)
        
        print('Received from client: %s' % data.decode('utf-8'))
        print('Sending the server time to client: %s' % ctime())
        try:
            client_sock.send(bytes(ctime(), 'utf-8'))
        except KeyboardInterrupt:
            print('Exited by user')
    sock.close() 