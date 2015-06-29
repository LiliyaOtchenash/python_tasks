class ListInstance:
  def __str__(self):
    return '<Instance of %s(%s), address %s: \n%s>' % (
      self.__class__.__name__,
      self.supers(),
      id(self),
      self.__attrnames())

  def __attrnames(self):
    result = ''
    for attr in sorted(self.__dict__):
      result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
    return result

  def supers(self):
    names = []
    for super in self.__class__.__bases__:
        print(super)
        names.append(super.__name__)
    return ', ' .join(names)

class Spam(ListInstance):
  def __init__(self):
    self.data1 = 'food'


class Sub(Spam): pass


x = Sub()
print(x)

str(x)
