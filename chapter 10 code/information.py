# creating class Person
class Person:
    # creating the __init__ function for the class with the attributes
    def __init__(self, name, address, age, number):
        # creating the attributes
        self.__name = name
        self.__address = address
        self.__age = age
        self.__number = number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        return self.__name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_number(self):
        return self.__number

    def set_number(self, number):
         self.__number = number
    # formating the employees information so that there aren't multiple print statements
    def  data(self):
        # calling on the attributes stated earlier in the class
        print(f'Name: {self.__name}')
        print(f'Address: {self.__address}')
        print(f'Age: {self.__age}')
        print(f'Phone Number: {self.__number}\n')