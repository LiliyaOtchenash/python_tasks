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
print("_" * 20)
def my_decorator(func):
    print('Im usual function')
    def wrapper():
        print('Im function that came back by decorator')
        func()
    return wrapper

def lazy_function():
    print('zzzzzzzzzzzzzzzzz')

decorated_function = my_decorator(lazy_function)

@my_decorator
def lazy_function():
    print('zzzzzzzzzzzzzzz')

lazy_function()
print('_' * 20)

def decorator_maker():
    print('I create decorators! I will call only once:'+\
          'When you ask me to create a decorator for you.')

    def my_decorator(func):
        print('Im decorator! I will be called once: at the moment of function decorating.')

        def wrapped():
            print('Im wrapper around decorating function.'
                  'I will be called every time when you call decorating function'
                  'I came back result of decorating function')
            return func()
        print('I came back wrappered function')
        return wrapped
    print('I came back decorator')
    return my_decorator

new_decorator = decorator_maker()
print('_' * 20)

def decorated_function():
    print('Im - decorated function')
decorated_function = decorator_maker()(decorated_function)
print(decorated_function())

print('_' * 20)

@decorator_maker()
def decorated_function():
    print('Im - decorated function')

print(decorated_function())
print('-' * 35)

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print('я создаю декораторы! я получил следующие аргументы: ', decorator_arg1,
          decorator_arg2)

    def my_decorator(func):
        print('Я - декратор. И ты передал мне эти аргументы', decorator_arg1,
              decorator_arg2)

        def wrapped(function_arg1, function_arg2):
            print('Я - обертка вокруг декорируемой функции.\n'
                  'И я имею доступ ко всем аргументам: \n'
                  '\t- и декоратора: {0} {1}\n'
                  '\t- и функции: {2}, {3}\n'
                  'Теперь я могу передать нужные аргументы дальше'
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)
        return wrapped
    return my_decorator


@decorator_maker_with_arguments('Леонард', 'Шелдон')
def decorated_function_with_arguments(function_arg1, function_arg2):
    print('аргументы функции: {0}, {1}'.format(function_arg1, function_arg2))

print('-' * 35)
decorated_function_with_arguments('Лилия', 'Отченаш')
print('-' * 35)


def decorator_with_args(decorator_to_enhance):
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)
        print('return decorator_wrapper')
        return decorator_wrapper
    print('return decorator_maker')
    return decorator_maker

@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print('Мне тут передали...', args, kwargs)

        return func(function_arg1, function_arg2)
    print('wrapper')
    return wrapper


@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print('Привет', function_arg1, function_arg2)

decorated_function('Вселенная и', 'все прочее')
print('_' * 30)


def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res
    return wrapper


def logging(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('log', func.__name__, args, kwargs)
        return res
    return wrapper


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print('{0} была вызвана: {1}x'.format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper


@benchmark
@logging
@counter
def reverse_string(string):
    return str(reversed(string))

print(reverse_string('KKKKKKKKeeeeppppppppp, fg, ggd,gdggddf'))

def reverse_string(string):
    return reversed(string)

print(reverse_string('a'))










