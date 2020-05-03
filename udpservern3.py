from socket import socket, AF_INET, SOCK_DGRAM

maxsize = 15000

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 12345))
while True:
    data, addr = sock.recvfrom(maxsize)
    print('client says:')
    print(data.decode())
    print('from: ')
    print(str(addr))
    resp = "UDP server sending data"
    sock.sendto(resp, addr)
    
