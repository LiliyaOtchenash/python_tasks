class tracer(object):
    def __init__(self, func):
        self.calls = 0
        self.func = func
        print('init tracer')

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        print('call')
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            print('wrapper')
            print(instance)
            return self(instance, *args, **kwargs)
        print('get')
        return wrapper
#Person.giveRaise = tracer(Person.giveRaise)
## init(Person.giveRaise, Person.give.Raise)
##    Person.giveRaise.calls = 0
##    Person.giveRaise.func = Person.giveRaise
##########  init tracer
###### lil.giveRaise
## get(Person.giveRaise, lil, tracer):
###########  get
## return wrapper
### wrapper(0.10)
############# wrapper
## return Person.giveRaise(lil, 0.1)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        print('init Person')

    @tracer          # выступает атрибутом класса Person
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
        print('giveRaise Person')


print('_' * 25)
lil = Person('LILI OTCHENACH', 120000)
print('_' * 25)
print(lil.giveRaise)
print('_' * 25)
lil.giveRaise(.10)
print('_' * 25)

@tracer
def spam(a, b, c):
    print(a + b + c)

# spam = tracer(spam)
# tracer(spam):
## __init(spam):
##  spam.calls = 0
##  spam.func = spam
########## init tracer
print(spam)
print(spam.calls)
print('_' * 25)


spam(1, 2, 3)
print('_' * 25)


