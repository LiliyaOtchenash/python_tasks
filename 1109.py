class tracer(object): # и декоратор и обертка
    def __init__(self, func):
        self.calls = 0
        self.func = func
        print('init')

    def __call__(self, *args, **kwargs): #при обращ к функции
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        print('_call tracer_')
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):#при обращ к атрибуту
        print('_get_')
        return wrapper(self, instance) #

class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj
        print('init wrapp')

    def __call__(self, *args, **kwargs):
        print('_call wrapp_')
        return self.desc(self.subj, *args, **kwargs)
# self = instance class wrapper
# desc = instance class Person
# subj = percent(arg in the method giveRaise)
@tracer
def spam(a, b, c):
    print(a + b + c)

spam(1, 2, 3)

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        print('init Person')

    @tracer          # выступает атрибутом класса Person
    def giveRaise(self, percent):
        print( '1 give raise tracer')
        self.pay *= (1.0 + percent)
        print('giveRaise Person')
         ## giveRaise = tracer(giveRaise) экз кл tracer
         ## == giveRaise.calls = 0
        ## == giveRaise.func = giveRaise
        ### init

lil = Person('LILI OTCHENACH', 120000)
## lil.name ='LILI OTCHENASH'
## lil.pay =  120000
### init Person
lil.giveRaise(.10)
## __get__(giveRaise, lil, tracer):
## wrappe(giveRaise, lil) == экз класса враппер
### 'get'
## __init__ (self_wrapper, giveRaise, lil)
##    self_wrapper.giveRaise = giveRaise
##    self_wrapper.lil = lil
### init wrap
## __call__(self_wrapper, 0.10) ===
##    giveRaise(lil, 0.10) == вызывает __call__  tracer
###    call 1 to giveRaise
### call tracer
###    call wrapp
### 1 give raise tracer
## lil.pay = lil.pay *(1 + 0.1) == 120000 * 1.1 =132000






#print(lil.pay)