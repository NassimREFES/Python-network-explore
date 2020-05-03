"""import sys, urllib.request

try:
    rfc_number = int(sys.argv[1])
except(IndexError, ValueError):
    print('Must sypply an rfc number as first argument')
    sys.exit(2)

template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()
print(rfc)"""

import sys, socket

try:
    rfc_number = int(sys.argv[1])
except(IndexError, ValueError):
    print('must supply an rfc number as first argument')
    sys.exit(2)
    
host = 'www.ietf.org'
port = 80
#link 
sock = socket.create_connection((host, port))

req = (
    'GET /rfc/rfc{rfcnum}.txt HTTP/1.1\r\n'
    'Host: {host}:{port}\r\n'
    'User-Agent: Python {version}\r\n'
    'Connection: close\r\n'
    '\r\n'
    )

req = req.format(rfcnum=rfc_number, host=host, port=port, version=sys.version_info[0])
#send request
sock.sendall(req.encode('ascii'))
#read()
rfc_raw = bytearray()
while True:
    buf = sock.recv(4096)
    if not len(buf):
        break
    rfc_raw += buf
rfc = rfc_raw.decode('utf-8')

print(rfc)