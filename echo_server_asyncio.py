import asyncio
import tincanchat

HOST = tincanchat.HOST
PORT = tincanchat.PORT

clients = []

class ChatServerProtocol(asyncio.Protocol):
    """ each instance of class represent a cleint and the socket connection to it """
    def connection_made(self, transport):
        """ called on instantiation, when new client connects """
        self.transport = transport
        self.addr = transport.get_extra_info('peername')
        self._rest = b''
        clients.append(self)
        print('Connection from {}'.format(self.addr))
        
    def data_received(self, data):
        """ handle data as its received, broadcast complete message to all other clients """
        data = self._rest + data
        (msgs, rest) = tincanchat.parse_recvd_data(data)
        self._rest = rest
        for msg in msgs:
            msg = msg.decode('utf-8')
            msg = '{}: {}'.format(self.addr, msg)
            print(msg)
            msg = tincanchat.prep_msg(msg)
            for client in clients:
                client.transport.write(msg)
                
    def connection_lost(self, ex):
        """ called on client disconnect, clean up client state """
        print('Client {} disconnected'.format(self.addr))
        clients.remove(self)
        
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # create server and initialize on the event loop
    coroutine = loop.create_server(ChatServerProtocol,
                            host=HOST, port=PORT)
    server = loop.run_until_complete(coroutine)
    # print listening socket info
    for socket in server.sockets:
        addr = socket.getsockname()
        print('Listening on {}'.format(addr))
        
    # run the loop to process client connections
    
    loop.run_forever()
    