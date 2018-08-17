from tornado import ioloop, gen
from time import time


@gen.coroutine
def ring():
    print("It's time to get up")


def later():
    print('time up')


if __name__ == '__main__':
    loop = ioloop.IOLoop.current()
    loop.call_at(time() + 2, ring)
    loop.call_later(0.1, later)
    loop.start()
