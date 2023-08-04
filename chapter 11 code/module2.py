# Creating Class Employee
class Employee:
    def __init__(self, name, number):
        # creating the attributes for Employee
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number
# creating the sublcass shiftsupervisor for class employee
class ShiftSupervisor(Employee):

    # calling the __init__ method and as well as the super() method for the sublcass
    def __init__(self, name, number, annual_salary, annual_bonus):
        super().__init__(name, number)

        # creating the attributes for ShiftSupervisor to use in the main function
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def get_annual_salary(self):
        return self.__annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    def get_annual_bonus(self):
        return self.__annual_bonus

    # adding __annual_salary and __annual_bonus together
    def calculate_bonus(self):
        # creating a total variable from the additin fo the two
        total = self.__annual_salary + self.__annual_bonus
        # returning the total
        return total
