

#self.stream.write('Game over\n', callback=self.stream.close)

class DBTCPServer(TCPServer):
    """TCP server for handling incoming connections from players"""

    def handle_stream(self, stream, address):
        """Called when new IOStream object is ready for usage"""
        logging.info('Incoming connection from %r', address)
        Connection(stream, address, server=self)

class Connection(object):
    """Player logic handler"""

    # Player's name. Should be setted for auth.
    name = None

    def __init__(self, stream, address, server):
        """Initialize base params and call stream reader for next line"""
        self.stream = stream
        if self.stream.socket.family not in (socket.AF_INET, socket.AF_INET6):
            # Unix (or other) socket; fake the remote address
            address = ('0.0.0.0', 0)
        self.address = address
        self.server = server
        self.stream.set_close_callback(self._on_disconnect)
        
        # Will block current stream flow until user's name is set
        # self.register(on_register=self.play)
        self.register(on_register=self.join)  

    def _on_read(self, line):
        """Called when new line received from connection"""
        # Some game logic (or magic)
        self.wait()

    def wait(self):
        """Read from stream until the next signed end of line"""
        self.stream.read_until(b("\n"), self._on_read)

    def _on_disconnect(self, *args, **kwargs):
        """Called on client disconnected"""
        logging.info('Client disconnected %r', self.address)
        self.unregister()

    def __str__(self):
        """Build string representation, will be used for working with
        server identity (not only name) in future"""
        return str(self.name)

def sig_handler(sig, frame):
    """Catch signal and init callback.
    
    More information about signal processing for graceful stoping 
    Tornado server you can find here:
    http://codemehanika.org/blog/2011-10-28-graceful-stop-tornado.html    
    """
    logging.warning('Caught signal: %s', sig)
    IOLoop.instance().add_callback(shutdown)

def shutdown(): 
    """Stop server and add callback to stop i/o loop"""
    io_loop = IOLoop.instance()

    logging.info('Stopping tcp server')
    io_loop.ttt.stop()

    logging.info('Will shutdown in 2 seconds ...')
    io_loop.add_timeout(time.time() + 2, io_loop.stop)

def main():
    """Main processing function"""
    io_loop = IOLoop.instance()

    # Create instance of Tic-Tac-Toe TCP server and save 
    # it as attribute of IOLoop instance. Of course, this 
    # is not the best way to spread ttt instance among 
    # several functions, but it's enough for demo app.
    io_loop.db_tcp_server = DBTCPServer()
    io_loop.db_tcp_server.listen(options.port)

    # Init signals handler for TERM and INT signals 
    # (and so KeyboardInterrupt)
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    logging.info('Starting tcp server on %d port', options.port)
    io_loop.start()


