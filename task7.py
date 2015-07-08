"""7 Композиция. Сымитируйте сценарий оформления заказа в  ресторане быстрого питания, определив четыре класса:
Lunch
Вмещающий и управляющий класс.
Customer
Действующее лицо, покупающее блюдо.
Employee
Действующее лицо, принимающее заказ
Food
То, что приобретает заказчик.
Чтобы вам было с чего начать, определите следующие классы и методы:

class Lunch:
    def __init__(self)                   # Создает и встраивает Customer и Employee
    def order(self, foodName)            # Имитирует прием заказа
    def result(self)                     # Запрашивает у клиента название блюда

class Customer:
    def __init__(self)                          # Инициализирует название блюда значением None
    def placeOrder(self, foodName, employee)    # Передает заказ официанту
    def printFood(self)                         # Выводит название блюда

class Employee:
    def takeOrder(self, foodName)               # Возвращает блюдо с указанным названием

class Food:
    def __init__(self, name)                         # Сохраняет название блюда
Имитация заказа работает следующим образом:
a. Конструктор класса Lunch должен создать и встроить экземпляр класса
Customer и экземпляр класса Employee, а кроме того, экспортировать ме-
тод с  именем order. При вызове этот метод должен имитировать прием
заказа у клиента (Customer) вызовом метода placeOrder. Метод placeOrder
класса Customer должен в  свою очередь имитировать получение блю-
да (новый объект Food) у официанта (Employee) вызовом метода takeOrder
класса Employee.
b.	 Объекты типа Food должны сохранять строку с названием блюда (напри-
мер, «буррито»), которое передается через Lunch.order в Customer.placeOr-
der, затем в Employee.takeOrder и, наконец, в конструктор класса Food. Кро-
ме того, класс Lunch должен еще экспортировать метод result, который
предлагает клиенту (Customer) вывести название блюда, полученного от
официанта (Employee) в результате выполнения заказа (этот метод может
использоваться для проверки имитации).
Обратите внимание: экземпляр класса Lunch должен передавать клиенту
(Customer) либо экземпляр класса Employee (официант), либо себя самого, что-
бы клиент (Customer) мог вызвать метод официанта (Employee).
Поэкспериментируйте с  получившимися классами в  интерактивной обо-
лочке, импортируя класс Lunch и вызывая его метод order, чтобы запустить
имитацию, а  также метод result, чтобы проверить, что клиент (Customer)
получил именно то, что заказывал. При желании можете добавить в файл
с классами программный код самотестирования, используя прием с атри-
бутом __name__ из главы 24. В этой имитации активность проявляет клиент
(Customer); как бы вы изменили свои классы, чтобы инициатором взаимодей-
ствий между клиентом и официантом был официант (Employee)?

"""

# экспортировать метод с  именем order.
class Lunch:
    def __init__(self):                      # создает и встраивает Customer и Employee
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName):               # имитирует прием заказа  
        self.cusromer.placeOrder(foodName)
    def result(self):                         # запрашивает у клиента название блюда 
        self.customer.printFood()

class Customer:                                      
    def __init__(self):                                # инициализирует название блюда значением None
        self.foodName = None
            
    def placeOrder(self, foodName, employee):           # передает заказ официанту
        self.foodName = Food(foodName)
        self.employee = Employee()
        Employee.takeOrder()     

    def printFood(self):                                 # выводит название блюда
        return self.foodName

class Employee:
    def takeOrder(self, foodName):                       # возвращает блюдо с указанным названием      
        thisfoodName = Foof(foodName)
        return thisfoodName   


class Food:
    def __init__(self, name):                            # сохраняет название блюда
        self.name = name


    
