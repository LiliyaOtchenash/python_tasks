def makebold(fn):
    def wrapped():
        print('раз')
        return '<b>' + fn() + '</b>'
    print('два')
    return wrapped

def makeitalic(fn):
    def wrapped():
        return '<b>' + fn() + '</i>'
    print('слушай Андрея')
    return wrapped


@makebold
@makeitalic
def hello():
    return 'hello habr'

#
# hello = makebold(makeitalic(hello))
# hello() уже внутри fn()

print(hello())

print('_' * 20)

def shout(word='да'):
    return word.capitalize()+'!!!'

print(shout())
scream = shout
print(scream())

del shout

try:
    print(shout())
except NameError:
    print('e')

print(scream())
print('_' * 20)


def talk():
    def whisper(word='да'):
        return word.lower()+'...'
    print(whisper())

talk()

try:
    print(whisper())
except NameError:
    print('tyt')

print('_' * 20)

def getTalk(type='shout'):
    def shout(word='yes'):
        return word.capitalize()+'!'

    def whisper(word='yes'):
        return word.lower()+'...'

    if type == 'shout':
        return shout
    else:
        return whisper

print(getTalk())
talk = getTalk()
print(talk)
print(talk())

print(getTalk('whisper'))
print(getTalk('whisper')())
print('_' * 20)

def doSomethingBefore(func):
    print('doSomethingBefore')
    print(func())

doSomethingBefore(scream)
print('_' * 20)

def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print('Я - код. который отработает до вызова функции')
        a_function_to_decorate()
        print('А я - код. срабатывающий после')
    return the_wrapper_around_the_original_function

def a_stand_alone_function():
    print('я простая функция. ты ведь не посмеешь меня изменить')

a_stand_alone_function()
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
print('_' * 20)

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
### a = decorator(a)
### a() = decoretor(a)()

print('_' * 20)
@my_shiny_new_decorator
def another_stand_alone_function():
    print('оставь меня в покое')

another_stand_alone_function()
print('_' * 20)

def bread(func):
    def wrapper():
        print('</--------\>')
        func()
        print('<\________/>')
    return wrapper

def ingredients(func):
    def wrapper():
        print('#tomatos#')
        func()
        print('~salads~')
    return wrapper

def sandwich(food='--beef--'):
    print(food)

print(sandwich())
sandwich = bread(ingredients(sandwich))
sandwich()
print('_' * 20)


def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print('смотри. что я получил:', arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print('Меня зовут', first_name, last_name)

print_full_name('Лилия','Отченаш')
print('_' * 20)


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3
        print('слушай Андрея внимательно')
        return method_to_decorate(self, lie)
    print('слушай Андрея')
    return wrapper



class Lucy(object):
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print('Мне %s, а ты бы сколько дал?' % (self.age + lie))
#sayYourAge =method_friendly_decorator(sayYourAge)
# sayYourAge = wrapper
l = Lucy()
print(l.age)
l.sayYourAge(-3) ### wrapper(l, -3)
##    lie = -3 - 3
##    sayYourAge(l, -6)
###       prin('Мне 32-6=26, а ты бы сколько дал?')

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('Перeдали ли мне что-нибудь?:')
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)
    print('обертка уже сработала func== a_wrapper_accepting_arbitrary_arguments')
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():  #####  почему ptint(args) срабатывает по разному как () и (<__main__.Mary object at 0x7fbb29f578d0>,)
    print('Python is cool, no argument here.')

function_with_no_argument()

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c, d='5'):
    print(a, b, c, d)

function_with_arguments(1, 2, 3, d='интересно')
print('_' * 20)

class Mary(object):
    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments   ###### почему print(args) срабатывает по разному  как () и как(<__main__.Mary object at 0x7fbb29f578d0>,)
    def sayYourAge(self, lie=-3):
        print('Мне %s. а ты бы сколько дал?' % (self.age + lie))

m = Mary()
m.sayYourAge()
# m.a_wrapper_accepring_arbitrary_arguments()
#











