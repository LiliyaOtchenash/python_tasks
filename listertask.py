# -*- coding: utf-8 -*-
"""
    согласно документации это не обязательно, но для обратной совместиаости с
    предыдущими версиями python, при использовании не ASCII символов в коде (русский)
    необходимо явно указывать кодировку (то, что я дописал в начале файла -> # -*- coding: utf-8 -*-)
"""
class ListTree:
    def __str__(self):
        self.__a = []
        self.__visited = {}
        print('1 self.__class__: ', self.__class__)        
        return '<Instance of {0}, addressss {1}{2}: \n{3}{4}>'.format(
            self.__class__.__name__,
            self.classtree(self.__class__),
            id(self),
            self.__attrnames(self, 0),
            self.__listclass(self.__class__, 4))

    def classtree(self, cls):
        self.__a.append(cls.__name__)
        for supercls in cls.__bases__: 
            classtree(supercls)  # <- classtree - это метод класса ListTree, как обращаться к методу класса внутри класса
        return self.__a
    #print(a)
    #print("Instances {0}({1})" .format(a[0], ','.join(a[1:])))

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        print('3 self.__visitet__: ', self.__visited)
        if aClass in self.__visited:                        
            return '\n{0}<Class {1}:, addres {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            #print('2 self.__class__.__bases__', aClass.__bases__) 
            #print('3 join', ''.join(genabove))                      
            genabove = (self.__listclass(c, indent+4)
                for c in aClass.__bases__)           
            return '\n{0}<Class {1}, addr {2}:\n{3}{4}{5}>\n'.format(  
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass, indent),
                ''.join(genabove),       
                dots)

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result


class Spam(ListTree):
    def __init__(self):
        self.data1 = 'food'
        self.data2 = 'clothes'


x = Spam()
print(x)


#Используя атрибут __bases__, расширьте классы в файле lister.py (глава 30) так, чтобы они выводили имена
#прямых суперклассов экземпляров класса. При этом первая строка в этом выводе должна выглядеть, как показано ниже (значение адреса у вас #может отличаться): <Instance of Sub(Super, ListTree), address 7841200:
