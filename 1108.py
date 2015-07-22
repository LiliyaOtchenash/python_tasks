def tracer(func):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall



@tracer
def spam(a, b, c):
    print(a + b + c)

spam(1, 2, 3)
spam(a=4, b=5, c=6)
print('-' * 20)
# spam = tracer(spam)
# spam(1, 2, 3) = tracer(spam(1, 2, 3))
# tracer(spam(1, 2, 3)
#     calls = 0
#     def onCall(*args, **kwargs)
### где эти аргументы беруться????)))

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
bob.giveRaise(.25)

