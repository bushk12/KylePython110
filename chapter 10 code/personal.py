# importing the information class
import information
# main function
def main():
    # creating the personal information to store in the information class to be formatted later
    chad = information.Person('Chad', '1234 Street Avenue', 32, '555-555-5552')
    bob = information.Person('Bob', "5678 Road Ave", 34, "518-988-1121")
    harry = information.Person('Harry', "9102 Road Ave", 35, '519-092-1234')
    # creating the instance chad and printing out the information
    information.Person.data(chad)
    # creating the instance bob and printing out the information
    information.Person.data(bob)
    # creating the instance harry and printing out the information
    information.Person.data(harry)
# calling the main function
if __name__ == '__main__':
    main()
