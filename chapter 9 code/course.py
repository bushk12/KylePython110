# importing the dictionary for the classlist
import classlist as cl
# importing some simple variables for printing format
import format_file as fl

# setting the global variables for the menu, I used the books "birthday" dictionary example for the menu options
CS101 = 1
CS102 = 2
CS103 = 3
NT110 = 4
CM241 = 5
QUIT = 6


def user_menu():
    # creating the menu
    print("===============================")
    print("Please Select From Below:")
    print("===============================")
    # user selection using the variables from above
    print("1.CS101")
    print("2.CS102")
    print("3.CS103")
    print("4.NT110")
    print("5.CM241")
    # giving the user an option to quit the program
    print("6.QUIT")
    print()


# main function
def main():
    # calling user_menu to print out the menu
    user_menu()
    # user choice pops up here. it will take a 1-6 option
    choice = int(input('Enter Your Choice: '))
    # in case a user doesn't use 1-6 it will ask again and again until they give the correct input
    while choice < CS101 or choice > QUIT:
        choice = int(input('Enter a valid choice:'))

    # if statement for the user
    # if the user chooses 1 it will print out the following
    if choice == CS101:
        print(fl.format)  # using the fl.format (see format_file.py)
        print('Course: CS101')
        print(fl.format)  # using the fl.format (see format_file.py)
        print(fl.number, cl.room['CS101'])  # cl.room is the imported module, it will grab the value of CS101
        print(fl.instructor, cl.inst['CS101'])  # cl.inst is the imported module, it will grab the value of CS101
        print(fl.time, cl.meet['CS101'])  # cl.meet is the imported module, it will grab the value of CS101
    # if the user chooses 2 it will print out the following. Same functionality as CS101, just calls for CS102 values
    if choice == CS102:
        print(fl.format)
        print('CS102')
        print(fl.format)
        print(fl.number, cl.room['CS102'])
        print(fl.instructor, cl.inst['CS102'])
        print(fl.time, cl.meet['CS102'])
    # if the user chooses 3 it will print out the following. Same functionality as CS101, just calls for CS103 values
    if choice == CS103:
        print(fl.format)
        print('CS101')
        print(fl.format)
        print(fl.number, cl.room['CS103'])
        print(fl.instructor, cl.inst['CS103'])
        print(fl.time, cl.meet['CS103'])
    # if the user chooses 4 it will print out the following. Same functionality as CS101, just calls for NT110 values
    if choice == NT110:
        print(fl.format)
        print('NT110')
        print(fl.format)
        print(fl.number, cl.room['NT110'])
        print(fl.instructor, cl.inst['NT110'])
        print(fl.time, cl.meet['NT110'])
    # if the user chooses 5 it will print out the following. Same functionality as CS101, just calls for CM241 values
    if choice == CM241:
        print(fl.format)
        print('CM241')
        print(fl.format)
        print(fl.number, cl.room['CM241'])
        print(fl.instructor, cl.inst['CM241'])
        print(fl.time, cl.meet['CM241'])
    # this allows the user to quit
    if choice == QUIT:
        exit()


if __name__ == '__main__':
    main()
