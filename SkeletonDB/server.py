#!/usr/bin/env python

import tornado.escape
import tornado.ioloop
import tornado.web
import os.path
import uuid
import json

from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options, parse_command_line


import ligneous
logger = ligneous.log("server")

import SkeletonDB
db = SkeletonDB.load()


define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("SkeletonDb Server")


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
        value = json.loads(value)
        db.set(key, value)
        self.write({"status":"ok"})


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
    )
    app.listen(options.port)
    logger.info("listing on port "+str(options.port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()


