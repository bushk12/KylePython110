# creating the class Employee
class Employee:
    def __init__(self, name, number):
        # creating the attributes for employee
        # attribute for name
        self.__name = name
        # attribute for number
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number


# making ProductionWorker a subclass of Employee
class ProductionWorker(Employee):

    def __init__(self, name, number, shift, pay_rate):
        super().__init__(name, number)
        # creating the attributes for shift and pay_rate for Prodcution Worker
        # attribute shift
        self.__shift = shift
        # attribute for pay_rate
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def set_shift(self, shift):
        self.__shift = shift

    def get_pay_rate(self):
        return self.__pay_rate

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate