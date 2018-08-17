from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado.httpserver import HTTPServer


class LoginHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_secure_cookie('username', 'wangj')
        self.write('login ok')
        self.finish()


class LogoutHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.clear_cookie('username')
        self.write('logout ok')
        self.finish()


class WhoHandler(web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('username') or 'unknown'
    @gen.coroutine
    def get(self):
        # username = self.get_secure_cookie('username') or 'unknown'
        username = self.current_user
        self.write('your username is %s' % (username,))
        self.finish()


application = web.Application([
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/whoami", WhoHandler),
    ], autoreload=True,
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")
# application.listen(8765)
server = HTTPServer(application)
server.bind(8765)
server.start()
IOLoop.current().start()
