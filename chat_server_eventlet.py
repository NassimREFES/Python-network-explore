import eventlet # use epoll and switch to select on windows os
import eventlet.queue as queue
import tincanchat

HOST = tincanchat.HOST
PORT = tincanchat.PORT
send_queues = {}

def handle_client_recv(sock, addr):
    """ receive message from client and broadcast them to other clients until client disconnects """
    rest = bytes()
    while True:
        try:
            (msgs, rest) = tincanchat.recv_msgs(sock)
        except (EOFError, ConnectionError):
            handle_disconnect(sock, addr)
            break
        for msg in msgs:
            msg = '{}: {}'.format(addr, msg)
            print(msg)
            broadcast_msg(msg)
            
def handle_client_send(sock, q, addr):
    """ monitor queue for new messages, sen them to client as they arrive """
    while True:
        msg = q.get()
        if msg == None: break
        try:
            tincanchat.send_msg(sock, msg)
        except (ConnectionError, BrokenPipeError):
            handle_disconnect(sock, addr)
            break
            
def broadcast_msg(msg):
    """ add message to each connected client's send queue """
    for q in send_queues.values():
        q.put(msg)
        
def handle_disconnect(sock, addr):
    """ ensure queue is cleaned up and socket closed when q client disconnect """
    fd = sock.fileno()
    q = send_queues.get(fd, None)
    if q:
        q.put(None)
        del send_queues[fd]
        addr = sock.getpeername()
        print('Client {} disconnected'.format(addr))
        sock.close()
        
if __name__ == '__main__':
    server = eventlet.listen((HOST, PORT))
    addr = server.getsockname()
    print('Listening on {}'.format(addr))
    
    while True:
        client_sock, addr = server.accept()
        q = queue.Queue()
        send_queues[client_sock.fileno()] = q
        eventlet.spawn_n(handle_client_recv,
                         client_sock,
                         addr)
        eventlet.spawn_n(handle_client_send,
                         client_sock,
                         q,
                         addr)
        print('Connection from {}'.format(addr))