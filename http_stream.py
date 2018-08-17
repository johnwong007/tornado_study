#http_stream.py
from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado.httpserver import HTTPServer


class ExampleHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        for _ in range(5):
            yield gen.sleep(1)
            self.write('zzzzzzzzzzzz&lt;br&gt;')
            self.flush()
        self.finish()

application = web.Application([
    (r'/example', ExampleHandler),
    ], autoreload=True)

# application.listen(8765)
server = HTTPServer(application)
server.listen(8765)
# server.bind(8765)
# server.start(1)

IOLoop.current().start()