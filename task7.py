class Lunch:
    def __init__(self):  # создает и встраивает Customer и Employee
        self.customer = Customer()
        self.employee = Employee()

    def order(self, foodName):  # имитирует прием заказа
        self.customer.placeOrder(foodName, self.employee)

    def result(self):  # запрашивает у клиента название блюда
        self.customer.printFood()


class Customer:
    def __init__(self):  # инициализирует название блюда значением None
        self.foodName = None

    def placeOrder(self, foodName, employee):  # передает заказ официанту
        self.foodName = employee.takeOrder(foodName)

    def printFood(self):     # выводит название блюда
        print(self.foodName.name)


class Employee:
    def takeOrder(self, foodName):  # возвращает блюдо с указанным названием
        return Food(foodName)


class Food:
    def __init__(self, name):  # сохраняет название блюда
        self.name = name


L = Lunch()
print(L.order('meat'))    # meat
print(L.result())
print(Food('fish'))  #<__main__.Food object at 0x7f583d479390>
C = Customer()
print(C.foodName) # None
