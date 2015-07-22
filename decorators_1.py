def makebold(fn):
    def wrapped():
        return '<b>' + fn() + '</b>'
    return wrapped

def makeitalic(fn):
    def wrapped():
        return '<b>' + fn() + '</i>'
    return wrapped


@makebold
@makeitalic
def hello():
    return 'hello habr'

# hello = makebold(makeitalic(hello))()
 ###  или hello = makebold(makeitalic(hello ()))