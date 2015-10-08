class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' %(self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a + b + c)

spam(1, 2, 3)
spam(1, 2, 3)
print(spam)
print(tracer)


# spam = tracer(spam)
# tracer(spam) - экземпляр класса tracer
#     def __init__(spam, spam):
#            spam.call = 0
 #           spam.func = spam
  #    def __call__(spam, (1, 2, 3)):
   #         spam.calls = 0 + 1
    #        print(call 1 to spam.spam.__name__)
     #       ==  call 1 to spam
      #      spam.spam(1, 2, 3) ==
       #     == 6