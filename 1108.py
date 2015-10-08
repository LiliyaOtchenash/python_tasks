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
# spam = tracer(spam) ==  return onCall == onCall
spam(1, 2, 3) # onCall(1, 2, 3)
### call 1 to spam
## return spam(1, 2, 3)
### 6
spam(a=4, b=5, c=6)
print('-' * 20)
#

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer# giveRaise = tracer(GiveRaise) ==return onCall = onCall
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    @tracer # == onCall
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
# sue.onCall(.10)
## call = 1
### call 1 to giveRaise
## return giveRaise(.10)
## sue.pay = sue.pay * (1.0 + 0.10) == sue.pay * 1.1= 110000
print(sue.pay)
print(bob.lastName())
## bob.onCall()
### call 1 to lastName
## return lastName() == bob.lastName()
### Smith

