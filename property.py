class Super:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('remove...')
        del self._name

    prop = property(getName, setName, delName, 'name property docs')


class Person(Super): pass


bob = Person('Bob Smith')
print(bob.prop)
bob.prop = 'Rober Smith'
print(bob.prop)
del bob.prop

print('_-_' * 25)
sue = Person('Sue Jones')
print(sue.prop)
print(Person.prop.__doc__)



