# importing module2, Class Employee & Sublcass ShiftSupervisor for the main function to work properly
import module2

def main():
    # asking for the user input for the information
    emp_name = input('Employee Name: ')
    emp_number = input('Employee Number: ')
    emp_salary = int(input('Employee Salary: '))
    emp_bonus = int(input('Employee Bonus: '))

    # creating an object for Class ShiftSupervisor to store and then output the data below
    bonus = module2.ShiftSupervisor(emp_name, emp_number, emp_salary, emp_bonus)
    print()

    # printing out the user input using the bonus object
    print('Name: ', bonus.get_name())
    print('Employee Number: ', bonus.get_number())
    print(f'Annual Salary: ${bonus.get_annual_salary()}')
    # grabbing teh total from def calculate_bonus from ShiftSupervisor Subclass
    print(f'Annual Bonus: ${bonus.calculate_bonus()}')

# Calling Main Function
if __name__ == '__main__':
    main()
