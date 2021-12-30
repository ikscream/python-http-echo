from time import sleep
from datetime import datetime

import os
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

class HHStorageHandler(RequestHandler):

    def get(self):
        print(self.request.__dict__)
        self.finish(f"{datetime.now()}: {self.request.remote_ip} {self.request.method} {self.request.path}\n")

port = os.environ.get('PORT', 8080)
print(f"echo server started on 0.0.0.0:{port}")
application = Application([(r".*", HHStorageHandler)])
server = HTTPServer(application)
server.bind(port)
server.start(1)
while True:
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        exit(0)
    except Exception as e:
        pass