# importing the empmod.py for class Employee
import empmod

# main function
def main():
    # creating variables for each employee, first value is the name, second is id, third is department, fourth is title
    emp1 = empmod.Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    # accessing the class employe from the python file empmod.py
    emp2 = empmod.Employee('Mark Jones', 39119, 'IT', 'Programmer')
    emp3 = empmod.Employee('Joy Rogers', 887114, 'Manufacturing', 'Engineering')

    # printing out the exercise name
    print("======================")
    print('Chapter 10 Exercise 4')
    print("======================")
    print()

    # calling back the function data from employee in empmod.py with the object emp1
    empmod.Employee.data(emp1)
    # calling back the function data from employee in empmod.py with the object emp2
    empmod.Employee.data(emp2)
    # calling back the function data from employee in empmod.py with the object emp3
    empmod.Employee.data(emp3)




# calling the main function
if __name__ == '__main__':
    main()
