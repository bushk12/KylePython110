# creating class Employee
class Employee:
    # creating the init function for the class
    def __init__(self, name, id_number, department, title):
        # calling all the attributes
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__title = title

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_id_number(self):
        return self.__id_number

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.__department

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    # creating the format for the data from the main function and calling each attribute
    def  data(self):
        print(f'Name: {self.__name}')
        print(f'ID Number: {self.__id_number}')
        print(f'Department: {self.__department}')
        print(f'Job Title: {self.__title}\n')