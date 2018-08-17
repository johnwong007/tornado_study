from tornado.ioloop import IOLoop
import tornado_mysql
from tornado import gen

@gen.coroutine
def testdb():
    conn = yield tornado_mysql.connect('localhost', 'root', 'Root#123', 'sdc')
    cursor = conn.cursor()
    yield cursor.execute('select login_name from login where id=10010', ())
    print(cursor.fetchone())


def test():
    pass

IOLoop.current().run_sync(testdb)
