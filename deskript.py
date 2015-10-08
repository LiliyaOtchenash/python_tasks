class Descriptor(object):
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:
    attr = Descriptor()


X = Subject()
#print(Subject)
#print('Descriptor:  ', Descriptor())
#print('X:   ', X)
#print('Subject():  ', Subject())
#print(X.attr)
#print(Subject.attr)


class D:
    def __get__(*args): print('get')
    def __set__(*args): raise AttributeError('cannot set')


class C:
    a = D()

X = C()
X.a
print(list(X.__dict__.keys()))
C.a
X.a = 99
print(X.a)
print(C.a)
print(list(X.__dict__.keys()))
Y = C()
Y.a
C.a
print(list(Y.__dict__.keys()))
