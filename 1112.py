import time

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kargs):
        start = time.clock()
        result = self.func(*args, **kargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@timer                           # listcomp = timer(listcomp)
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return map((lambda x: x * 2), range(N))


result = listcomp(5)
listcomp(5000)
listcomp(50000)
listcomp(100000)
print(result)
print('allTime = %s' % listcomp.alltime)
