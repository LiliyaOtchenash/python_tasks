class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('can`t get attribute')
        return  self.fget(instance)
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('cant set attribute')
        self.fget(instance, value)

    def __delete__(self, instance):
        if self.fset is None:
            raise AttributeError('cant delete attribute')
        self.fdel(instance)


    class Person:
        def getName(self):

