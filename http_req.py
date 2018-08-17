from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado.httpclient import AsyncHTTPClient
from tornado.httpserver import HTTPServer

url = 'http://hq.sinajs.cn/list=sz000001'


class GetPageHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        client = AsyncHTTPClient()
        response = yield client.fetch(url, method='GET')
        self.write(response.body.decode('gbk'))
        self.finish()


application = web.Application([
    (r"/getpage", GetPageHandler),
], autoreload=True)
# application.listen(8765)
server = HTTPServer(application)
server.bind(8765)
server.start()
IOLoop.current().start()
