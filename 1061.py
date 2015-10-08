class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def getSquare(self):
        return self._square ** 2

    def setSquare(self, value):
        self._square = value

    squaree = property(getSquare, setSquare)

    def getCube(self):
        return  self._cube ** 3

    cube = property(getCube)


X = Powers(3, 4)
print(X.squaree)
print(X.cube)
X.squaree = 5
print(X.squaree)
print('_' * 20)


class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2

    def __set__(self, instance, value):
        instance._square = value


class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3


class Powers:
    square = DescSquare()
    cube = DescCube()
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)
print('_' * 20)


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr:' + name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value   # просто добавить новый атрибут с заначением в класс

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)
print('_' * 20)


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)






