from socket import socket, AF_INET, SOCK_DGRAM

maxsize = 4096
port = 12345

if __name__ == '__main__':
    sock = socket(AF_INET, SOCK_DGRAM)
    msg = "Hello UDP server"
    sock.sendto(msg.encode(), ('', port))
    data, addr = sock.recvfrom(maxsize)
    print('Server says:')
    print(repr(data))
    print('from: ')
    print(str(addr))