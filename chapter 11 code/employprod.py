# importing module one for Class Employee and sublcass ProductionWorker
import module1

# main function
def main():
    # asking for user input on these four variables
    emp_name = input('Employee Name: ')
    emp_number = input('Employee Number: ')
    shift_number = int(input('Enter Shift Number (1/2): '))
    hourly_rate = float(input('Enter Hourly Pay Rate: '))
    # creating the worker object out of the production worker subclass
    worker = module1.ProductionWorker(emp_name, emp_number, shift_number, hourly_rate)

    print()
    # printing out the information inputted by the user, grabbing the attributes (mutators and accessors) from the Class
    print('Name: ', worker.get_name())
    print('Employee Number: ', worker.get_number())
    print('Shift Number: ', worker.get_shift())
    print(f'Hourly Pay Rate: ${worker.get_pay_rate()}')

# calling the main function
if __name__ == '__main__':
    main()
