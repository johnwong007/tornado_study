from tornado import ioloop, gen, iostream
from tornado.tcpclient import TCPClient


@gen.coroutine
def trans():
    stream = yield TCPClient().connect('localhost', 8760)
    try:
        for msg in ('zjsadkfj', 'jjjjj', 'jkkkkkk', 'over'):
            yield stream.write(msg)
            back = yield stream.read_bytes(20, partial=True)
            print back
    except:
        pass

ioloop.IOLoop.current().run_sync(trans)
