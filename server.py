from time import sleep

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

class HHStorageHandler(RequestHandler):

    def get(self):
        print(self.request.__dict__)
        self.finish(self.request.path)

application = Application([(r".*", HHStorageHandler)])
server = HTTPServer(application)
server.bind(20000)
server.start(1)
while True:
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        pass