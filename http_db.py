# http_db.py
from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado_mysql import pools
import tornado_mysql
from tornado.httpserver import HTTPServer
import MySQLdb

connParams = {'host': '127.0.0.1', 'user': 'root', 'passwd': 'Root#123', 'db': 'sdc'}


class GetUserHandler(web.RequestHandler):
    # host = 'localhost'
    # port = 3306
    # usr = 'root'
    # passwd = 'Root#123'
    # db = 'sdc'
    # POOL = pools.Pool(
    #     dict(host=host, port=port, user=usr, passwd=passwd, db=db),
    #     max_idle_connections=1,
    #     max_recycle_sec=3,
    # )

    @gen.coroutine
    def get(self):
        userid = self.get_argument('id')
        # cursor = yield self.POOL.execute('select login_name from login where id=10010')
        # conn = yield tornado_mysql.connect(host='localhost', port=3306, user='root', passwd='Root#123', db='sdc')
        # cursor = conn.cursor()
        # yield cursor.execute('select login_name from login where id=10010', ())

        db = MySQLdb.connect("localhost", "root", "Root#123", "sdc", charset='utf8')
        cursor = db.cursor()
        cursor.execute('select login_name from login where id=%s', (userid, ))
        res = cursor.fetchone()
        if res:
            self.write({"status": 1, "name": res[0]})
        else:
            self.write({"status": 0, "name": ""})

        self.finish()

    @gen.coroutine
    def post(self):
        pass


application = web.Application([
    (r"/getuser", GetUserHandler),
], autoreload=False)
# application.listen(8765)
server = HTTPServer(application)
server.bind(8765)
server.start(1)
IOLoop.current().start()
