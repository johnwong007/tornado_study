from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado.httpserver import HTTPServer


class ExampleHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        delay = self.get_argument('delay', 5)
        yield gen.sleep(int(delay))
        self.write({"status":1, "msg":"success", "delay":delay})
        self.finish()

    @gen.coroutine
    def post(self):
        pass

print('=>>>>>>>>>>>>>>>>>>>>>>>>>> application start')

application = web.Application([
    (r"/example", ExampleHandler),
    #(r"/other", OtherHander),
    ],autoreload=True)
# application.listen(8765)
server = HTTPServer(application)
server.bind(8765)
server.start(1)
IOLoop.current().start()

print('=>>>>>>>>>>>>>>>>>>>>>>>>>> application end')
