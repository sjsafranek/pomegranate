
from tornado.ioloop import IOLoop
# from tornado.iostream import IOStream
from tornado.tcpserver import TCPServer

import ligneous
logging = ligneous.log("tcp")

import database
db = database.load()

import utils

class Connection(object):
	
	def __init__(self, stream, address):
		#print(dir(address))
		#logging.info('receive a new connection from %s', address)
		self.name = None
		self.uuid = utils.short_uuid()
		self.stream = stream
		self.address = address
		self.stream.set_close_callback(self._on_close)
		self.stream.read_until(b"\n", self._on_read_line)
		self.stream.write(b"SkeletonDb Tcp Server", self._on_write_complete)
		self.stream.write(b"skeleton!> ", self._on_write_complete)
	
	def _on_read_line(self, data):
		logging.info("[%s] %s", self.uuid, data)
		
		data = data.rstrip()
		cmd = data.decode("utf-8").split(" ")
		
		if "exit" == cmd[0]:
			self.stream.socket.close()
			return

		message = 'skeleton!> {}\n'
		
		if 2 == len(cmd):
			if "get" == cmd[0]:
				result = db.get(cmd[1])
				message = message.format(result)
			elif "remove" == cmd[0]:
				if db.remove(cmd[1]):
					message = message.format('{"success":"ok"}')
				else:
					message = message.format('{"success":"fail"}')

		if 3 == len(cmd):
			if "set" == cmd[0]:
				if db.set(cmd[1], cmd[2]):
					message = message.format('{"success":"ok"}')
				else:
					message = message.format('{"success":"fail"}')

		if 'skeleton!> {}\n' != message:
			self.stream.write(message.encode(), self._on_write_complete)
	
		self.stream.write(b"skeleton!> ", self._on_write_complete)
	
	def _on_write_complete(self):
		if not self.stream.reading():
			self.stream.read_until(b"\n", self._on_read_line)
	
	def _on_close(self):
		logging.info("[%s] connection closed", self.uuid)


class Server(TCPServer):

	def __init__(self, io_loop=None, ssl_options=None, **kwargs):
		logging.info('tcp server is started')
		TCPServer.__init__(self, io_loop=io_loop, ssl_options=ssl_options, **kwargs)

	def handle_stream(self, stream, address):
		Connection(stream, address)


def main():
	chat_server = Server()
	chat_server.listen(8888)
	chat_server.start(0)
	IOLoop.instance().start()


if __name__ == '__main__':
	main()
