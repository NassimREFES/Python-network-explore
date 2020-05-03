import socket

HOST = 'www.python.org'
PORT = 80
BUFSIZE = 4096
ADDR = (HOST, PORT)

if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(ADDR)
    
    obj = open('file.txt', 'w')
    
    while True:
        data = 'GET / HTTP/1.0\r\nHost: python.org \r\n\r\n'
        if not data:
            break
        client_sock.send(data.encode('utf-8'))
        data = client_sock.recv(BUFSIZE)
        obj.write(str(data.decode('utf-8')))
        if not data:
            break
        print(data.decode('utf-8'))
        
    client_sock.close()
    obj.close()