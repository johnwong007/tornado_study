from tornado import gen,ioloop

times = 0
callback_handler = None
@gen.coroutine
def count():
    print('1 second has gone')
    global times
    times = times+1
    if times>1:
        callback_handler.stop()

if __name__=='__main__':
    callback_handler = ioloop.PeriodicCallback(count, 1000)
    callback_handler.start()
    ioloop.IOLoop.current().start()