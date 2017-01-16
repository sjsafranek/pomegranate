#!/usr/bin/env python

import os.path
import json
import logging

import tornado.web
import tornado.log
import tornado.autoreload
# import tornado.escape
from tornado.ioloop import IOLoop
# from tornado.iostream import IOStream
from tornado.tcpserver import TCPServer
from tornado.concurrent import Future
from tornado.options import define
from tornado.options import options
from tornado.options import parse_command_line


#import ligneous
#http_logger = ligneous.log("http")
#tcp_logger = ligneous.log("tcp")

import database
db = database.load()

import utils


#logger.LogFormatter("%(asctime)s [%(levelname)s] [%(name)s] %(filename)s line:%(lineno)d : %(message)s")
def log_function(handler):
    info = {
        'status': handler.get_status(),
        'method': handler.request.method,
        'url': handler.request.uri,
        'remote_ip': handler.request.remote_ip,
        'duration': (handler.request.request_time()*1000)
    }
    log_extra = logging.LoggerAdapter(logging.getLogger("tornado.access"),
            info)
    log_extra.info(info)


# Command line arguments
define("port", default=8000, help="http run on the given port", type=int)
define("tcp", default=5816, help="tcp run on the given port", type=int)
define("debug", default=False, help="run in debug mode")


# HTTP SERVER
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("SkeletonDb Http Server")


class GetHandler(tornado.web.RequestHandler):
    def get(self, key):
        self.write({
            "status": "ok",
            "data": {
                "result": db.get(key)
            }
        })


class SetHandler(tornado.web.RequestHandler):
    def post(self, key):
        value = self.request.body.decode("utf-8")
        try:
            value = json.loads(value)
        except:
            pass
        db.set(key, value)
        self.write({"status":"ok"})


# TCP SERVER
class Connection(object):
    
    def __init__(self, stream, address):
        self.name = None
        self.uuid = utils.short_uuid()
        self.stream = stream
        self.address = address
        self.stream.set_close_callback(self._on_close)
        self.stream.read_until(b"\n", self._on_read_line)
        self.stream.write(b"SkeletonDb Tcp Server\n", self._on_write_complete)
        self.stream.write(b"skeleton!> ", self._on_write_complete)
    
    def _on_read_line(self, data):
        #tcp_logger.info("[%s] %s", self.uuid, data)
        
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
        tcp_logger.info("[%s] connection closed", self.uuid)


class Server(TCPServer):

    def __init__(self, io_loop=None, ssl_options=None, **kwargs):
        #tcp_logger.info("*** tcp listing on port "+str(options.tcp))
        TCPServer.__init__(self, io_loop=io_loop, ssl_options=ssl_options, **kwargs)

    def handle_stream(self, stream, address):
        Connection(stream, address)




def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/api/v1/get/([a-zA-Z0-9_]+)", GetHandler),
            (r"/api/v1/set/([a-zA-Z0-9_]+)", SetHandler),
        ],
        # cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        # template_path=os.path.join(os.path.dirname(__file__), "templates"),
        # static_path=os.path.join(os.path.dirname(__file__), "static"),
        # xsrf_cookies=True,
        debug=options.debug,
        #log_request=log_function,
    )
    app.log_request = log_function
    app.listen(options.port)
    #http_logger.info("*** http listing on port "+str(options.port))
    
    chat_server = Server()
    chat_server.log_request = log_function
    chat_server.listen(options.tcp)
    #chat_server.start(0)

    tornado.autoreload.start()
    IOLoop.instance().start()
    #IOLoop.current().start()


if __name__ == "__main__":
    main()



