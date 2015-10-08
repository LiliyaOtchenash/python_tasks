class Person:
    def __init__(self, name):
        self._name = name
    @property          # dec = property(dec)
    def dec(self):
        'name property docs'
        print('fetch...')
        return self._name

    @dec.setter          # name = name.setter(name)
    def dec(self, value):
        print('changes...')
        self._name = value

    @dec.deleter          # name =name.deleter(name)
    def dec(self):
        print('remove...')
        del self._name

bob = Person('Bob Smith')
print(bob.dec)   #
bob.dec = 'Robert Smith'
print(bob.dec)   #
del bob.dec

print("-" * 20)
sue = Person('Sue Jones')
print(sue.dec)
print(Person.dec.__doc__)